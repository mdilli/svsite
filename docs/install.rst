
Installation
===============================

svSite should provide a fully functional site with minimal work.

Although later on you may want to personalize the look (:doc:`info <layout>`), which will take time. That's inevitable.

To get svSite running, follow the steps in the appropriate section.

Linux / bash
-------------------------------

For this to work, you will need ``python3-dev`` including ``pip`` and a database (``sqlite3`` is default and easy, but slow). Things will be easier and better with ``virtualenv`` (or ``pew``) and ``git``, so probably get those too. You'll also need ``libjpeg-dev`` and the dev version of Python because of ``pillow``. You can install them with::

	sudo apt-get install python3-dev sqlite3 python-virtualenv git libjpeg-dev

Get the code. The easiest way is with git, replacing ``SITENAME``::

	git clone https://github.com/mverleg/svsite.git SITENAME

Enter the directory (``cd SITENAME``). Starting a virtual environment is recommended::

	virtualenv -p python3 env
	source env/bin/activate

If you skip this step, everything will be installed system-wide, so you need to prepend ``sudo`` before any `pip` command::

	pip install --editable .

If you want to run tests, build the documentation or do anything other than simply running the website, or if you want to make sure you have the correct versions, you should install (otherwise skip it)::

	pip install -r dev/pip_freeze.txt  # optional

We need a database. SQLite is used by default, which you could replace now or later (in ``source/svsite/settings_local.py``) for a substantial performance gain. To create the structure and an administrator, type this and follow the steps::

#todo: migrate in two steps
#todo: ./manage.py bower install
#todo: need npm

	python3 source/manage.py migrate
	python source/manage.py createsuperuser

Then there's static files, which are handles by bower. It has some dependencies [#foot1]_ ::

	sudo apt-get install nodejs
	npm install bower
	cd dev; bower install; cd ..
	python source/manage.py collectstatic --noinput

Then you can start the testserver. This is not done with the normal ``runserver`` command but with ::

	python3 source/manage.py runserver_plus --cert dev/cert YOUR_URL

We use this special command to use a secure connection, which is enforced by default. In this test mode, an unsigned certificate is used, so you might have to add a security warning.

Make sure to replace ``YOUR_URL``, or leave it out to run on localhost. You can stop the server with ``ctrl+C``.

To **(re)start the server** later, go to the correct directory and run::

	source env/bin/activate  # only if you use virtualenv
	python3 source/manage.py runserver_plus --cert dev/cert YOUR_URL

Note that this is just for development! When the website is going live, you should probably use a webserver such as Apache.

.. rubric:: Footnotes

.. [#foot1] If you don't want to install node and bower, you can easily download the packages listed in `dev/bower/json` by hand and put them in `env/bower`. Make sure they have a `dist` subdirectory where the code lives. Make sure to still run the last command if you do this.


