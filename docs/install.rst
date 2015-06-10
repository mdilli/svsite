
Installation
===============================

svSite should provide a fully functional site with minimal work.

Although later on you may want to personalize the look (:doc:`info <layout>`), which will take time. That's inevitable.

To get svSite running, follow the steps in the appropriate section.

Linux / bash
-------------------------------

For this to work, you will need ``python3`` including ``pip`` and a database (``sqlite3`` is default and easy, but slow). Things will be easier and better with ``virtualenv`` and ``git``, so probably get those too. You can install them with::

	sudo apt-get install python3 sqlite3 python-virtualenv git

Get the code. The easiest way is with git, replacing ``SITENAME``::

	git clone https://github.com/mverleg/svsite.git SITENAME

Enter the directory (``cd SITENAME``). Starting a virtual environment is recommended::

	virtualenv -p python3 env
	source env/bin/activate

If you skip this step, everything will be installed system-wide, so you need to preprend ``sudo`` before any `pip` command::

	pip install --editable .

If you want to run tests, build the documentation or do anything other than simply running the website, or if you want to make sure you have the correct versions, you should install (otherwise skip it)::

	pip install -r dev/pip_freeze.txt  # optional

We need a database. SQLite is used by default, which you could replace now or later (in ``source/svsite/settings_local.py``) for a substantial performance gain. To create the structure and an administrator, type this and follow the steps::

	python3 source/manage.py migrate
	python source/manage.py createsuperuser

Then you can start the server by using::

	python3 source/manage.py runserver YOUR_URL

Make sure to replace ``YOUR_URL``, or leave it out to run on localhost. You can stop the server with ``ctrl+C``. To run with extra debug functionality, if you installed the extra packages, you can use ``runserver_plus`` instead of ``runserver``.

To **(re)start the server** later, got to the correct directory and run::

	source env/bin/activate  # only if you use virtualenv
	python3 source/manage.py runserver YOUR_URL  # or runserver_plus


