
Contribute
===============================

Say you want to make some changes. Perhaps they turn out great, and you want to share them. That is greatly appreciated, and this page tells you how to do it!

Linux / bash
-------------------------------

You will need to make sure you `can push`_ code to Github by setting up ssh keys. Then fork the svsite repository and follow these steps.

You will need ``python3``, ``pip``, a database (``sqlite3`` is default and easy, but slow), ``virtualenv``, ``git``, ``elasticsearch`` and some SSL packages. Just type::

	sudo apt-get install python3 sqlite3 python-virtualenv git build-essential libssl-dev libffi-dev python-dev elasticsearch

Get your copy of the svsite code::

	git clone git@github.com:YOUR_SVSITE_FORK.git

Go to the directory, start a virtualenv and install::

	virtualenv -p python3 env
	source env/bin/activate
	pip install --requirement dev/pip_freeze.txt
	pip install --no-deps --editable .

To create the database and superuser::

	python3 source/manage.py migrate
	python3 source/manage.py createsuperuser

You might want to run the tests::

	py.test tests

Then you can start the server on localhost::

	python3 source/manage.py runserver_plus --cert dev/cert

You can now open the site in a browser. It is running on localhost over https on port 8000. The server prepends ``www``, so use a domain that works with that prefix. For example,

	https://www.localhost.markv.nl:8000/

This refers to your localhost (127.0.0.1). The first time you will probably need to add a security exception, as this is a debug SSL certificate.

Now you are ready to make your chances!

After you are done and have tested your changes (and converted space-indents to tabs), you can suggest it for inclusion into svsite by means of a `pull request`_

A general note
-------------------------------


Good luck! why-we-never-forget-our-fellow-coders_

.. _can push: https://help.github.com/articles/generating-ssh-keys/
.. _pull request: https://help.github.com/articles/creating-a-pull-request/
.. _why-we-never-forget-our-fellow-coders http://www.commitstrip.com/en/2014/11/21/why-we-never-forget-our-fellow-coders/

