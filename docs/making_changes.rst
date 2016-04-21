
Making changes
===============================

svSite should let you get a site running with a (somewhat) limited amount of work. But perhaps there are still some details you want to change. And you can! Given some knowledge of Django (features) and/or html/css/js (layout), you can create your copy of the code and occasionally get updates from the main project.

And perhaps your changes turn out great, and you want to share them. That is greatly appreciated, and this page tells you how to do it!

.. _contribute:

Contribute
-------------------------------

You can contribute by adding to the project! This includes:

* Contribute a :doc:`theme <layout>`
* Add features (in_ the project or :doc:`external <integration_api>`)
* Bugfixes (see issues_)
* Tests
* Documentation

Making changes
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

	python3 source/manage.py runserver_plus --settings=base.settings_development

You can now open the site in a browser. It is running on localhost over https on port 8443.

If ``www.`` is prepended, you can use a domain that works with that prefix (not ``localhost:8443``). For example,

	https://www.localhost.markv.nl:8443/

This refers to your localhost (127.0.0.1). The first time you will probably need to add a security exception, as this is a debug SSL certificate.

Now you are ready to make your chances!

After you are done and have tested your changes (and converted space-indents to tabs), you can suggest it for inclusion into svsite by means of a `pull request`_

External services
-------------------------------

There is a minimal api for building external services, which is described in :doc:`integration_api`. Such additions are welcome, you're encouraged to notify us when you complete one!

Automated tests
-------------------------------

Automatic testing is currently very limited for the project. We use ``py.test`` ones, which can be stored in ``/test/`` or ``source/$app/test``. It's greatly appreciated if you add more, for your own additions or for existing code. It'll help ensure the quality of the codebase!

A general note
-------------------------------

Good luck! `Why we never forget our fellow coders`_

.. _can push: https://help.github.com/articles/generating-ssh-keys/
.. _pull request: https://help.github.com/articles/creating-a-pull-request/
.. _`Why we never forget our fellow coders`: http://www.commitstrip.com/en/2014/11/21/why-we-never-forget-our-fellow-coders/
.. _in: https://github.com/mverleg/svsite/issues
.. _issues: https://github.com/mverleg/svsite/issues


