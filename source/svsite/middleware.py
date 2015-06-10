
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


SSL = 'SSL'

class HttpsRedirectMiddleware():
	"""
		Make sure all http requests are redirected to https .

		Adapted from https://djangosnippets.org/snippets/85/
	"""
	def process_view(self, request, view_func, view_args, view_kwargs):
		if not self._is_secure(request):
			return self._redirect(request)

	def _is_secure(self, request):
		if request.is_secure():
			return True
		#Handle the Webfaction case until this gets resolved in the request.is_secure()
		if 'HTTP_X_FORWARDED_SSL' in request.META:
			return request.META['HTTP_X_FORWARDED_SSL'] == 'on'
		return False

	def _redirect(self, request):
		newurl = '{0:s}://{1:s}{2:s}'.format('https', request.get_host(), request.get_full_path())
		if settings.DEBUG and request.method == 'POST':
			raise RuntimeError('Django can\'t perform a SSL redirect while maintaining POST data. Please structure your views so that redirects only occur during GETs.')
		return HttpResponsePermanentRedirect(newurl)


