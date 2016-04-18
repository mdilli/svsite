
from django.conf.urls import url
from intapi.views import api_info, user_list_api, team_list_api, user_details_api, team_details_api


urlpatterns = [
	url(r'^$', api_info),
	url(r'^members/$', user_list_api, name='user_list_api'),
	url(r'^member/$', user_details_api, name='user_details_api'),
	url(r'^teams/$', team_list_api, name='team_list_api'),
	url(r'^team/$', team_details_api, name='team_details_api'),
]



