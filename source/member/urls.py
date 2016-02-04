
from django.conf.urls import url
from member.views import member_profile, member_profile_me


urlpatterns = [
	url(r'^me/$', member_profile_me, name='member_profile_me'),
	url(r'^$', member_profile, name='profile_info'),
	url(r'^(?P<pk>\d+)/$', member_profile, name='profile_info'),  #todo: use slug instead of id
	url(r'^(?P<pk>\d+)-(?P<label>[-\w]+)/$', member_profile, name='profile_info'),
	url(r'^login_register/$', lambda request: None, name='profile_settings'),  # todo: already implemented?
]


