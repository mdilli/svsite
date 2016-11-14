
Going live - Upstart
===============================

On Ubuntu and related systems, it used to be that ``Upstart`` was the way to get and keep a process running. These days it's recommended to transition to ``systemd``, so please :doc:`do that<install_live>` if unless you have an old version of Ubuntu. You are? Then you can read this...

Here is an example configuration file, which should go in ``/etc/init//svsite.conf``::

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
		/path_to_virtualenv/bin/python3.5 source/manage.py runmodwsgi --log-to-terminal --user www-data --group devs --host=localhost --port 8081 --pythonpath=/path_to_virtualenv/svsite/lib/python3.5/site-packages source/wsgi.py
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

If both ``svsite`` and ``apache2`` are running, you should then be able to visit your site!

:doc:`Go back to the rest of the setup guide<install_live>`.


