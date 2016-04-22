
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


