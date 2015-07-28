
from django.http import HttpResponse
from django.shortcuts import render


def notification(request, message, title = None, next = None):
	return render(request, 'notification.html', {
		'message': message,
		'title': title,
		'next': next,
	})



