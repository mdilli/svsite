from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def birthdays_plugin_overview(request):
	return HttpResponse('it works!')