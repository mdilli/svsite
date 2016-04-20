
Going live
===============================

There are many ways to make a Django site accessible to the world. The method in the `official documentation`_ is using ``Apache`` and ``mod_wsgi``. You're free to use any method.

wsgi
-------------------------------

This is the "normal" wsgi way. It is explained in the `official documentation`_. This section is just an example of a complete Apache configuration file. Where to put this depends on your operating system and setup; for Ubuntu it's in ``/etc/apache2/sites-available/svsite`` (then do ``a2ensite svsite`` and ``sudo service apache2 reload``)::

	!! This is the port for HTTPS; use :80 when not using https
	<VirtualHost *:4433>
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
		WSGIDaemonProcess svsite python-path=/live/svsite/source:/home/mark/.virtualenvs/svsite/lib/python3.4/site-packages
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

	!! This handles HTTP resquests, by sending all of them to HTTPS
	!! (When not using HTTPS, remove this and change the other one to port :80)
	<VirtualHost *:80>
		ServerName domain.com
		ServerAlias *.domain.com

		Redirect permanent / https://domain.com/
	</VirtualHost>

A downside of this method is that all your websites must use the same python; you can't have one using python2 and another using python3. This will often not be a problem, but if it is, use another method, like the next one.

wsgi-express
-------------------------------

The method described here is a variation on the official one. It also uses ``Apache`` and ``mod_wsgi``, but ``mod_wsgi`` is part of Python instead of Apache. An advantage of this setup is that you can have different websites with different Python versions, which is not otherwise possible.


First, install ``mod_wsgi`` in your virtual environment (:doc:`remember <install_dev>` the ``pew`` stuff?)::

	pip install mod_wsgi

You can test that it works with::

	mod_wsgi-express start-server source/wsgi.py --port 8001  # optionally: --group devs

which should let you visit `localhost:8001`_ and see the site. If it does not work, have a look at `mod_wsgi pypi page`_




.. _`official documentation`: https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
.. _`localhost:8001`: http://localhost:8001/
.. _`mod_wsgi pypi page`: https://pypi.python.org/pypi/mod_wsgi


