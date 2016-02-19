
"""
Inspired by https://github.com/clutchio/clutch/blob/master/django_ext/http.py but some changes:

- Use json instead of simplejson, see http://stackoverflow.com/questions/712791/what-are-the-differences-between-json-and-simplejson-python-modules/
- Minetype doesn't depend on DEBUG; that seems like it's create very annoying bugs with no benefit.
- Allow the encoder, mimetype and indent to be changed.
- Callback removed until it's needed... Not very sure if that should be generally available...
"""

from json import dumps
from django.conf import settings
from django.http import HttpResponse


class JSONResponse(HttpResponse):
	def __init__(self, request, data, indent = 2 if settings.DEBUG else None, status_code = 200,
			content_type = 'application/json', mime = None, **json_kwargs):
		if mime is not None:
			content_type = mime
		content = dumps(data, indent = indent, **json_kwargs)
		super(JSONResponse, self).__init__(content = content, content_type = content_type, status = status_code)


