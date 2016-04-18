
Integration
===============================

There is a ``https-json`` api for integrating external tools. It provides read-only access to information about users (``member``s) and groups (``team``s).

Server setup
-------------------------------



https

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

If all goes well, the result will be a string containing a ``JSON`` list or map. Otherwise you will get an error message and a non-200 status code.

As an example (Bash terminal, but others like PHP_ should be similar):

.. code-block:: bash

    $ curl --show-error --request POST 'https://domain.com/$intapi/members/' --data-urlencode "key=abc123"
    [
      "mark",
      "henk"
    ]

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


