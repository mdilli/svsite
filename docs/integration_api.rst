
Integration
===============================

There is a ``https-json`` api for integrating external tools. It provides read-only access to information about users (``member``s) and groups (``team``s).

Server setup
-------------------------------

To allow client services access to some member and team info through the http api, you only need to change a few settings.

These settings should go in ``local.py``, since they are installation dependent and should not be accessible to outsiders.

* Add setting ``INTEGRATION_KEYS``, which should be a list of keys:

	.. code-block:: python

		INTEGRATION_KEYS = [
		  'abc123',      # php widget
		  'password!',   # android app
		]

  It is advisable to add a new key for each service, so that you can revoke them individually, if the need arises. Generate keys at random.org_ .

* Add setting ``INTEGRATION_ALLOW_EMAIL`` which can be ``True`` or ``False`` (the default). Services can only request a list of email addresses if this is ``True`` (option ``email=yes``). Otherwise, services can only get a user's email when that user logs in to the service.

* Restart the server.

Also note that, though ``https`` is always important, it is even more important with this api, since both api keys and user credentials and info will be sent over plain ``http`` if you don't have a secure connection.

External tool setup
-------------------------------

To get the information, send a ``POST`` request to one of the API urls. The urls for your server can be found at an info page for the server, which is usually ``/$intapi/``. This is the info  send to each of the urls:

+---------------+-----------------------+-------------------------------------+--------------------+--------------------------------+
| Info          | Default url           | Input                               | Output             | Note                           |
+===============+=======================+=====================================+====================+================================+
| (info page)   | ``/$intapi/members/`` | (nothing)                           | url & config info  | can use ``GET``                |
+---------------+-----------------------+-------------------------------------+--------------------+--------------------------------+
| Member list   | ``/$intapi/members/`` | ``key``, optionally ``email=yes``   | list of usernames  | if email, dict username->email |
+---------------+-----------------------+-------------------------------------+--------------------+--------------------------------+
| Member        | ``/$intapi/member/``  | ``key``, ``username``, ``password`` | user info map      | can authenticate if successful |
+---------------+-----------------------+-------------------------------------+--------------------+--------------------------------+
| Team list     | ``/$intapi/teams/``   | ``key``                             | team name list     | no hidden teams                |
+---------------+-----------------------+-------------------------------------+--------------------+--------------------------------+
| Team          | ``/$intapi/team/``    | ``key``, ``teamname``               | team info map      | works for hidden teams         |
+---------------+-----------------------+-------------------------------------+--------------------+--------------------------------+

The option ``email=yes`` only works if the server has ``INTEGRATION_ALLOW_EMAIL`` set to ``True``.

If all goes well, the result will be a string containing a ``JSON`` list or map. Otherwise you will get an error message and a non-200 status code.

It is recommended that you associate the relevant user data with that user's session in a safe way (rather than store it in a database), as you will get a fresh copy each time the users logs in.

As an example (Bash terminal, but others like PHP_ should be similar):

.. code-block:: bash

	$ curl --show-error --request POST 'https://domain.com/$intapi/members/' --data-urlencode "key=abc123"
	[
	  "mark",
	  "henk"
	]

.. code-block:: bash

	$ curl --show-error --request POST 'https://domain.com/$intapi/members/' --data-urlencode "key=abc123" --data-urlencode "email=yes"
	{
	  "mark": "mark@spam.la",
	  "henk": ""
	}

.. code-block:: bash

	$ curl --show-error --request POST 'https://domain.com/$intapi/member/' --data-urlencode "key=abc123" --data-urlencode "username=mark" --data-urlencode "password=drowssap"
	{
	  "username": "mark",
	  "first_name": "Mark",
	  "last_name": "V",
	  "email": "mark@spam.la",
	  "birthday": null,
	  "teams": {
		"Tokkies": "Mastersjief"
	  }
	}

.. code-block:: bash

	$ curl --show-error --request POST 'https://domain.com/$intapi/teams/' --data-urlencode "key=abc123"
	[
	  "Tokkies"
	]

.. code-block:: bash

	$ curl --show-error --request POST 'https://domain.com/$intapi/team/' --data-urlencode "key=abc123" --data-urlencode "teamname=Tokkies"
	{
	  "hidden": false,
	  "teamname": "Tokkies",
	  "description": "You know, from TV?",
	  "leaders": [
		"mark"
	  ],
	  "members": {
		"mark": "Mastersjief"
	  }
	}

Good luck!

.. _PHP: http://stackoverflow.com/questions/5647461/how-do-i-send-a-post-request-with-php
.. _random.org: https://www.random.org/passwords/?num=5&len=24&format=html&rnd=new


