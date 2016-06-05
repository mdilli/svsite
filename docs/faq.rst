
Frequently...
===============================

...asked questions
-------------------------------

How can I contribute?
...............................

Okay, this one hasn't been asked "frequently" in the strict meaning of the word, but anyway. Glad you're interested! Your help is welcome! Please check the :ref:`contribute section <contribute>`.

...encountered problems
-------------------------------

* After updating, you might get::

    KeyError at /en/stuff/
    'SomethingPlugin'

  This means a plugin was removed but is still in the database. Just run::

    python source/manage.py cms delete_orphaned_plugins --noinput

  if you were using the plugin that was removed, then those use cases will be gone. The alternative is reverting the update.

ElasticSearch / Haystack can't connect
---------------------------------------

You can test that elasticsearch is running using a http request on port 9200, like so::

    curl -X GET http://127.0.0.1:9200

If it isn't, there could be a number of reasons.

In my case, I had to set ``START_DAEMON=true`` in /etc/default/elasticsearch (source_)

You might also have the wrong version of the Python binding, see here_


.. _here: http://stackoverflow.com/questions/28257502/cant-get-elasticsearch-working-with-django/33138244#33138244
.. _source: https://discuss.elastic.co/t/cant-start-elasticsearch-with-ubuntu-16-04/48730/8


