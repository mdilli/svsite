
from django.http import HttpResponsePermanentRedirect
from os.path import basename


class HardAddSlashStripWwwMiddleware():
	"""
		Like APPEND_SLASH, and opposite of APPEND_WWW.
		It does not check whether the page exists.
	"""
	def process_request(self, request):
		if request.META['HTTP_HOST'].lower().find('www.') == 0:
			return HttpResponsePermanentRedirect(request.build_absolute_uri().replace('//www.', '//'))
		if not request.path.endswith('/'):
			if not '.' in basename(request.path):
				get = request.GET.urlencode()
				new = '{0:s}/{1:s}{2:s}'.format(request.path, '?' if get else '', get)
				return HttpResponsePermanentRedirect(new)


