
Going live
===============================

There are many ways to make a Django site accessible to the world. The method in the `official documentation`_ is using ``Apache`` and ``mod_wsgi``. You're free to use any method.

The one described here is a variation on the official one. It also uses ``Apache`` and ``mod_wsgi``, but ``mod_wsgi`` is part of Python instead of Apache. An advantage of this setup is that you can have different websites with different Python versions, which is not otherwise possible.

wsgi-express
-------------------------------

First, install ``mod_wsgi`` in your virtual environment (:doc:`remember <install_dev>` the ``pew`` stuff?)::

	pip install mod_wsgi

You can test that it works with::

	mod_wsgi-express start-server source/wsgi.py --port 8001  # optionally: --group devs

which should let you visit `localhost:8001`_ and see the site. If it does not work, have a look at `mod_wsgi pypi page`_



.. _`official documentation`: https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
.. _`localhost:8001`: http://localhost:8001/
.. _`mod_wsgi pypi page`: https://pypi.python.org/pypi/mod_wsgi


