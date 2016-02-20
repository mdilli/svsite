
from json import dumps
from cms.utils import get_language_code
from django.http import HttpResponse
from django.conf import settings
from django.utils.translation import get_language
from haystack.constants import DEFAULT_ALIAS
from haystack.routers import BaseRouter


class JSONResponse(HttpResponse):
	"""
	Inspired by https://github.com/clutchio/clutch/blob/master/django_ext/http.py but some changes:

	- Use json instead of simplejson, see http://stackoverflow.com/questions/712791/what-are-the-differences-between-json-and-simplejson-python-modules/
	- Minetype doesn't depend on DEBUG; that seems like it's create very annoying bugs with no benefit.
	- Allow the encoder, mimetype and indent to be changed.
	- Callback removed until it's needed... Not very sure if that should be generally available...
	"""
	def __init__(self, request, data, indent = 2 if settings.DEBUG else None, status_code = 200,
			content_type = 'application/json', mime = None, **json_kwargs):
		if mime is not None:
			content_type = mime
		content = dumps(data, indent = indent, **json_kwargs)
		super(JSONResponse, self).__init__(content = content, content_type = content_type, status = status_code)


class LanguageSearchRouter(BaseRouter):
	"""
	Based on Aldryn search.
	"""
	def for_read(self, **hints):
		language = get_language_code(get_language())
		if language not in settings.HAYSTACK_CONNECTIONS:
			return DEFAULT_ALIAS
		return language

	def for_write(self, **hints):
		language = get_language_code(get_language())
		if language not in settings.HAYSTACK_CONNECTIONS:
			return DEFAULT_ALIAS
		return language


