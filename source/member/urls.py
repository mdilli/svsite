
from django.conf.urls import url
from member.views import member_profile, member_profile_me


urlpatterns = [
	url(r'^me/$', member_profile_me, name = 'member_profile_me'),
	url(r'^(?P<pk>\d+)/$', member_profile, name = 'member_profile'),
	url(r'^(?P<pk>\d+)-(?P<label>[-\w]+)/$', member_profile, name = 'member_profile'),
]


