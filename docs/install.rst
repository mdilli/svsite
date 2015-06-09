
Installation
===============================

svSite should provide a fully functional site with minimal work. Although later on you may want to personalize the look, which will take time. That's inevitable.

To get svSite running, follow the steps in the appropriate section.

Linux / bash
-------------------------------

For this to work, you will need `python3` including `pip` and a database (`sqlite3` is default and easy, but slow). Things will be easier and better with `vritualenv` and `git`, so probably get those too.

Get the code. The easiest way is with git, replacing ``SITENAME``::

	git clone https://github.com/mverleg/svsite.git SITENAME

Enter the directory (``cd SITENAME``). Starting a virtual environment is recommended::

	virtualenv env
	source env/bin/activate

If you skip this step, everything will be installed system-wide, so you need to preprend ``sudo`` before any `pip` command::

	pip install -e .

If you want to run tests, build the documentation or do anything other than simply running the website, or if you want to make sure you have the correct versions, you should install (otherwise skip it)::

	pip install -r dev/pip_freeze.txt

We need a database. SQLite is used by default, which you could replace now or later (in ``source/svsite/settings_local.py``) for a substantial performance gain. To populate, type this and follow the steps::

	python3 source/manage.py syncdb

Then you can start the server with using::

	python3 source/manage.py runserver YOUR_URL

Make sure to replace ``YOUR_URL``, or leave it out to run on localhost.

You can stop the server with ``ctrl+C``. To run with extra debug functionality, if you installed the extra packages, you can use ``runserver_plus`` instead of ``runserver``.

To **(re)start the server** later, got to the correct directory and run::

	source env/bin/activate  # only if you use virtualenv
	python3 source/manage.py runserver YOUR_URL  # or runserver_plus


