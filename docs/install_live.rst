
Going live
===============================

There are many ways to make a Django site accessible to the world. The method in the `official documentation`_ is using ``Apache`` and ``mod_wsgi``. You're free to use any method. After setting up the server with https, don't forget to check the second part of the document on how to set up a secure``https`` connection.

Server (no https yet)
-------------------------------

wsgi
...............................

This is the "normal" wsgi way. It is explained in the `official documentation`_. This section is just an example of a complete Apache configuration file. Where to put this depends on your operating system and setup; for Ubuntu it's in ``/etc/apache2/sites-available/svsite`` (then do ``a2ensite svsite`` and ``sudo service apache2 reload``)::

	<VirtualHost *:80>
		ServerName domain.com
		ServerAlias *.domain.com

		Options -Indexes

		# PLACE HTTPS STUFF HERE. More on that later.

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

A downside of this method is that all your websites must use the same python; you can't have one using python2 and another using python3. It also allows you to restart Django without root privileges. These might be unimportant, but if they are, use another method, like the next one.

wsgi-express
...............................

This alternative method is a variation on the official one. It also uses ``Apache`` and ``mod_wsgi``, but ``mod_wsgi`` is part of Python instead of Apache. An advantage of this setup is that you can have different websites with different Python versions, which is not otherwise possible.

This relies on ``mod_wsgi``, which should already be installed in your virtual environment (otherwise, :doc:`remember <install_dev>` the ``pew`` stuff? Do that and ``pip install mod_wsgi``). Furthermore, ``'mod_wsgi.server',`` needs to be in ``INSTALLED_APPS``, svsite already does this for you.

You can test that it works with (user and group are optional, it's safe to use the correct permissions when live later though)::

	python source/manage.py runmodwsgi --log-to-terminal --user www-data --group devs --host=localhost --port 8081 --pythonpath=/path-to-virtualenv/lib/python3.4/site-packages source/wsgi.py

which should let you visit `localhost:8081`_ and see the site. If it does not work, have a look at `mod_wsgi pypi page`_.

The idea is to run a wsgi server, and let Apache proxypass the requests to it. Here is an example of the Apache settings for a non-HTTPS setup (which should be added later). Depending on your setup, this might belong in ``/etc/apache2/sites-available/svsite``::

	<VirtualHost *:80>
		ServerName domain.com
		ServerAlias *.domain.com

		Options -Indexes

		# PLACE HTTPS STUFF HERE. More on that later.

		# This is for static files, which should be served by Apache without Django's help
		# There is some cache stuff, which you can turn off by removing it.
		# Need to make a ProxyPass exception, since ProxyPass is handled
		# before Alias so it swallows everything otherwise.
		Alias /static /data/static/svsite
		ProxyPass /static !
		<Directory /data/static/svsite/>
			ExpiresActive On
			ExpiresDefault "access plus 1 day"
			Header append Cache-Control "public"
			Options -Indexes
			Order deny,allow
			Allow from all
		</Directory>

		# Media is similar to static, but without cache.
		# (note that anyone can access any files if they have the url)
		Alias /media /data/media/svsite
		ProxyPass /media !
		<Directory /data/media/svsite/>
			Options -Indexes
			Order deny,allow
			Allow from all
		</Directory>

		# This is the core part: all the non-static traffic is just sent to wsgi.
		# `retry=0` causes Apache to retry to contact wsgi every time, even if it got no response last time
		ProxyPass / http://localhost:8081/ retry=0
		ProxyPassReverse / http://localhost:8081/

		# Apache logs (don't forget to set up logging in Django settings).
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

	# make sure the wsgi process is gone, otherwise you can't restart
	post-stop script
	    kill $(cat /var/run/svleo.pid)
	    rm -f /var/run/svleo.pid
	end script

After saving this, you can use these self-explanatory commands::

	sudo service svsite status
	sudo service svsite start
	sudo service svsite stop

If both ``svsite`` and ``apache2`` are running, you should then be able to visit your site! What happens is that you visit it on port 80 (or 443 after the next section) and it arrives at Apache. In case of static or media files, Apache sends the files (possibly with caching headers). Otherwise, it asks the wsgi server on port 8081 for the page, which Django responds.

The server should *not* be reachable on port 8081 (`http://domain.com:8081/`) from the outside words. You might also want to check that the wsgi server (and apache and the database) automatically start on reboot (by rebooting).

Secure connection (https)
-------------------------------

After using one of the setup methods, it's highly recommended that you set up a secure connection. Now that letsencrypt_ offers free certificates (donations appreciated), there are few good excuses left not to. One method will be documented, but there are many.

Apache & letsencrypt
...............................

This section will explain how to do it for ``Apache`` with ``letsencrypt``, so it can be used with either of the above setups. There are other options, which are documented online.

First, generate a certificate (more details here_) by running the following commands), answering as appropriate. This will place ``letsencrypt`` in the current directory, so move to the directory where you want it first.::

	# get the code and stop Apache
	git clone https://github.com/letsencrypt/letsencrypt
	cd letsencrypt
	sudo service apache2 stop
	# request the certificate (change the domains)
	sudo ./letsencrypt-auto certonly --standalone -d domain.com -d www.domain.com

The certificate files should be stored in ``/etc/letsencrypt/live/domain.com/`` (with your domain). If the above command reports another location, use that.

Now we need to update the Apache configuration. First, change the port in the first line from ``80`` to ``443``::

	<VirtualHost *:80>   # old one
	<VirtualHost *:443>  # new one

Place the below (with updated paths) in your Apache config inside the ``<VirtualHost *:443>`` (as marked with a comment above)::

	SSLEngine on
	SSLCertificateFile /etc/letsencrypt/live/domain.com/cert.pem
	SSLCertificateKeyFile /etc/letsencrypt/live/domain.com/privkey.pem
	SSLCertificateChainFile /etc/letsencrypt/live/domain.com/chain.pem
	# Header always set Strict-Transport-Security "max-age=2600000; preload"

And at the bottom add (if you want all requests to be secure)::

	<VirtualHost *:80>
		ServerName domain.com
		ServerAlias *.domain.com

		Redirect permanent / https://domain.com/
	</VirtualHost>

The last line tells browsers to not access your site through http for a long time. Only enable it when you are confident things are working and will keep working! It's good for security, making it hard for attackers to divert traffic to http, but it'll make your site inaccessible if https stops working.

Now just restart Apache and see if things work::

	sudo service apache2 restart

You can update ``local.py`` with (at least)::

	SESSION_COOKIE_SECURE = CSRF_COOKIE_SECURE = False

You'll need to refresh your https certificates every few months. Don't forget to do that!

.. _`official documentation`: https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
.. _`localhost:8081`: http://localhost:8081/
.. _`mod_wsgi pypi page`: https://pypi.python.org/pypi/mod_wsgi
.. _letsencrypt: https://letsencrypt.org/
.. _here: https://letsencrypt.org/getting-started/


