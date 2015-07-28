
from django.shortcuts import render


def error_view(request, message, title = None, next = None, status = 400)
	"""
		:param status:

			* 400 and subset mean something was wrong with the request (e.g. user error; this request will never work)
			* 500 and subset mean server error (might work after it's fixed)
			* See more: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
	"""
	return render(request, 'error.html', {
		'message': message,
		'title': title,
		'next': next,
	}, status = status)


def csrf_failure(request, reason):
	return error_view(request,
		message = 'There was a problem with the ',
	)


