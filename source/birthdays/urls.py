
from django.conf.urls import url
from birthdays.views import birthdays_plugin_overview


urlpatterns = [
	url(r'^birthdays/$', birthdays_plugin_overview, name='birthdays_plugin_overview'),
]


