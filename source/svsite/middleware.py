from os import environ
from django.core.exceptions import MiddlewareNotUsed
from svsite import settings
from django.http import HttpResponsePermanentRedirect


assert not getattr(settings, 'PREPEND_WWW', False), \
	'the settings PREPEND_WWW cannot both be true when RemoveWWW middleware is enabled'


class RemoveWwwMiddleware():
	"""
		Opposite of PREPEND_WWW, which will apparently never be added to Django.

		Largely from https://gist.github.com/dryan/290771
	"""
	def process_request( self, request ):
		try:
			if request.META['HTTP_HOST'].lower().find('www.') == 0:
				from django.http import HttpResponsePermanentRedirect
				return HttpResponsePermanentRedirect(request.build_absolute_uri().replace('//www.', '//'))
		except:
			pass


