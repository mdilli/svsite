
from django.conf.urls import url
from member.views import team_info_all, team_info


urlpatterns = [
	url(r'^$', team_info_all, name='team_info_all'),
	url(r'^(?P<slug>[-\w]+)/$', team_info, name='team_info'),
]



