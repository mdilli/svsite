
Design notes (hacks)
===============================

Some parts are less than elegant. Although, at the time of writing, it seems there may not be a better way, it warrants a warning anyway.

Migrating
-------------------------------

Clean migrations don't quite work for some cms addons. Find the :doc:`migration info <install>` in the installation documentation.

Themes
-------------------------------

`Djangocms` seems not designed to handle dynamic templates, so a fixed template is used that dynamically includes the theme template based on a context variable.

Since `djangocms` uses `sekizai`, which must have it's `render_block` be in the top template, it is necessary to have the `<head>` and `<body>` in this top template, and to include only the rest of the content of these tags.

Furthermore, the CMS does some kind of pre-render without context to find the placeholders to be filled. This means placeholders cannot depend on the theme (=context). Placeholders are defined in ``default_body.html`` and themes should match those.

Special pages
-------------------------------

This relates to those pages (e.g. search results) that should not be plugins in the CMS, but should be integrated into it anyway (to be in the menu, be moved and allow placeholders).

What I would have preferred to do would be to have such pages (as apphooks) extend the main template and overwrite ``{% block content %}``.
However, because of themes, ``{% block content %}`` is necessarily defined in an ``{% include %}`` file.
Django cannot extend blocks defined in included files (regrettably) since they are each rendered separately (not so much 'included'), making the block useless.

The 'solution' used is to force templates to include a dynamic template instead of the `content` placeholder for such pages.
::

	{% if page_include %}
		{% include page_include %}
	{% else %}
		{% placeholder "content" %}
	{% endif %}

There is a special version of `render`, namely `base.render_cms_special`, that you can use like this:
::

	def my_view(request):
		value = 'do some query or something'
		return render_cms_special(request, 'my_template.html', dict(
			key=value,
		))

It is important to note that ``my_template.html`` in this example should render *just* the content part, not the full page. Don't ``{% extend %}`` the base template (or anything, for that matter); this is done automatically.


