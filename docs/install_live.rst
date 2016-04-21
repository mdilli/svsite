
Going live
===============================

There are many ways to make a Django site accessible to the world. The method in the `official documentation`_ is using ``Apache`` and ``mod_wsgi``. You're free to use any method.

wsgi
-------------------------------

This is the "normal" wsgi way. It is explained in the `official documentation`_. This section is just an example of a complete Apache configuration file. Where to put this depends on your operating system and setup; for Ubuntu it's in ``/etc/apache2/sites-available/svsite`` (then do ``a2ensite svsite`` and ``sudo service apache2 reload``)::

	!! This is the port for HTTPS; use :80 when not using https
	<VirtualHost *:443>
		ServerName domain.com
		ServerAlias *.domain.com

		Options -Indexes

		# This is HTTPS stuff, which is optional but important
		# https://www.digicert.com/ssl-support/apache-multiple-ssl-certificates-using-sni.htm
		#SSLEngine on
		#SSLCertificateFile /etc/apache2/TLS/markv.nl.crt
		#SSLCertificateKeyFile /etc/apache2/TLS/markv.nl.key
		#SSLCertificateChainFile /etc/apache2/TLS/markv.nl.ca-bundle
		#Header always set Strict-Transport-Security "max-age=2600000; preload"

		# Run WSGI in daemon mode (separate process for each Django site)
		# python-path should point to your virtual environment
		# /live/svsite should be the location of your code
		WSGIDaemonProcess svsite python-path=/path_to_virtualenv/lib/python3.4/site-packages
		WSGIProcessGroup svsite
		WSGIScriptAlias / /live/svsite/source/wsgi.py

		# This is for static files, which should be served by Apache without Django's help
		# There is some cache stuff, which you can turn off by removing it
		Alias /static/ /data/static/svsite/
		<Directory /data/static/svsite/>
			ExpiresActive On
			ExpiresDefault "access plus 1 day"
			Header append Cache-Control "public"
			Options -Indexes
			Order deny,allow
			Allow from all
		</Directory>

		# Media is similar to static, but without cache
		# (note that anyone can access any files if they have the url)
		Alias /media/ /data/media/svsite/
		<Directory /data/media/svsite/>
			Options -Indexes
			Order deny,allow
			Allow from all
		</Directory>

		# If you want to protect files but let Apache serve them, use Xsend
		# XSendFile On
		# XSendFilePath /data/media/svsite/

		# Apache logs (don't forget to set up logging in Django settings)
		LogLevel info
		ErrorLog ${APACHE_LOG_DIR}/svsite-error.log
		CustomLog ${APACHE_LOG_DIR}/svsite-access.log common
	</VirtualHost>

	# This handles HTTP resquests, by sending all of them to HTTPS
	# (When not using HTTPS, remove this and change the other one to port :80)
	<VirtualHost *:80>
		ServerName domain.com
		ServerAlias *.domain.com

		Redirect permanent / https://domain.com/
	</VirtualHost>

A downside of this method is that all your websites must use the same python; you can't have one using python2 and another using python3. It also allows you to restart Django without root privileges. These might be unimportant, but if they are, use another method, like the next one.

wsgi-express
-------------------------------

This alternative method is a variation on the official one. It also uses ``Apache`` and ``mod_wsgi``, but ``mod_wsgi`` is part of Python instead of Apache. An advantage of this setup is that you can have different websites with different Python versions, which is not otherwise possible.


This relies on ``mod_wsgi``, which should already be installed in your virtual environment (otherwise, :doc:`remember <install_dev>` the ``pew`` stuff? Do that and ``pip install mod_wsgi``).

You can test that it works with (user and group are optional, it's safe to use the correct permissions when live later though)::

	python source/manage.py runmodwsgi --log-to-terminal --user www-data --group devs --host=localhost --port 8081 --pythonpath=/path-to-virtualenv/lib/python3.4/site-packages source/wsgi.py

which should let you visit `localhost:8081`_ and see the site. If it does not work, have a look at `mod_wsgi pypi page`_.

The idea is to run a wsgi server, and let Apache proxypass the requests to it. Here is an example of the Apache settings for a non-HTTPS setup (which should be added later). Depending on your setup, this might belong in ``/etc/apache2/sites-available/svsite``::

    <VirtualHost *:80>
        ServerName domain.com
        ServerAlias *.domain.com

        Options -Indexes

        # This is for static files, which should be served by Apache without Django's help
        # There is some cache stuff, which you can turn off by removing it
        Alias /static/ /data/static/svsite/
        <Directory /data/static/svsite/>
            ExpiresActive On
            ExpiresDefault "access plus 1 day"
            Header append Cache-Control "public"
            Options -Indexes
            Order deny,allow
            Allow from all
        </Directory>

        # Media is similar to static, but without cache
      	# (note that anyone can access any files if they have the url)
        Alias /media/ /data/media/svsite/
        <Directory /data/media/svsite/>
            Options -Indexes
            Order deny,allow
            Allow from all
        </Directory>

        # This is the core part: all the non-static traffic is just sent to wsgi.
        # `retry=0` causes Apache to retry to contact wsgi every time, even if it got no response last time
        ProxyPass / http://localhost:8081/ retry=0
        ProxyPassReverse / http://localhost:8081/

        # Apache logs (don't forget to set up logging in Django settings)
        LogLevel info
        ErrorLog ${APACHE_LOG_DIR}/svsite-error.log
        CustomLog ${APACHE_LOG_DIR}/svsite-access.log common
    </VirtualHost>

Use ``a2ensite svsite`` and ``sudo service apache2 reload``.

Then we need to make sure that the wsgi server is always running. There are many ways. On Ubuntu and possibly other related systems, one can use Upstart. Here is an example configuration file, which should go in ``/etc/init/svsite``::

    description "Always run the wsgi daemon for svsite website"

    # automatically start on boot
    start on filesystem or runlevel [2345]

    # automatically stop on shutdown
    stop on shutdown or runlevel [!2345]

    # restart if it stops for any reason other than you manually stopping it
    respawn

    # this is the code that starts the process (update the parths and user/group)
    script
        cd /live/svsite
        /path_to_virtualenv/bin/python3.4 source/manage.py runmodwsgi --log-to-terminal --user www-data --group devs --host=localhost --port 8081 --pythonpath=/path_to_virtualenv/svsite/lib/python3.4/site-packages source/wsgi.py
    end script

After saving this, you can use these self-explanatory commands::

    sudo service svsite status
    sudo service svsite start
    sudo service svsite stop

If both ``svsite`` and ``apache2`` are running, you should then be able to visit your site! What happens is that you visit it on port 80 and it arrives at Apache. In case of static or media files, Apache sends the files (possibly with caching headers). Otherwise, it asks the wsgi server on port 8081 for the page, which Django responds.

The server should *not* be reachable on port 8081 (`http://domain.com:8081/`) from the outside words. You might also want to check that the wsgi server (and apache and the database) automatically start on reboot (by rebooting).


.. _`official documentation`: https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
.. _`localhost:8081`: http://localhost:8081/
.. _`mod_wsgi pypi page`: https://pypi.python.org/pypi/mod_wsgi


