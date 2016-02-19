
Layout
===============================

svSite should provide a fully functional site (with :doc:`minimal work <install>`), but you may want to personalize the look, which will take time. That's inevitable. Here is some information on how to do it.

Theme requirements
-------------------------------

To create your own theme, these are the requirements:

* The files should be organized into directories ``templates``, ``static`` and ``info``:

	* The ``templates`` directory should contain ``base.html`` holding the theme body and optionally ``head.html`` holding anything in ``<head>`` (you might want to include ``default_head.html``). Except for that, it can contain any templates you want (these are only used if you explicitly include them).
	* The ``static`` directory should contain any static files you use (see below on how to use them).
	* The ``info`` directory can contain any of these files: ``readme.rst``, ``description.rst``, ``credits.rst`` and ``license.txt``. Other files can be included but nothing special happens with them.

*
	Include static css/js files using:
	::

		{% load addtoblock from sekizai_tags %}
		{% addtoblock "css" %}
			<link rel="stylesheet" href="{% static THEME_PREFIX|add:'/css/style.css' %}">
		{% endaddtoblock "css" %}

	and other static files:
	::

		{% load static from staticfiles %}
		<img src="{% static THEME_PREFIX|add:'/logo.png' %}" />

	You can also hard-code ``{% static 'theme_name/logo.png' %}``. This behaves differently in case another theme extends this one.

*
	For the ``base.html`` template:

	* It should not extend anything (it is itself included).
	* It should define precisely these placeholders:
	::

		{% placeholder "header" %}
		{% placeholder "top-row" %}
		{% placeholder "content" %}
		{% placeholder "sidebar" %}
		{% placeholder "bottom-row" %}

	* It should ``{% include include_page %}`` if it's set, e.g. a structure like this:
	::

		{% if page_include %}
			{% include page_include %}
		{% else %}
			{% placeholder "content" %}
		{% endif %}

	* You do not need to define ``{% block %}`` . You won't be able to extend them since Django doesn't let you extend blocks from included templates.


