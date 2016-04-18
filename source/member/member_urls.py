
from django.conf.urls import url
from member.views import member_profile_all, member_profile, member_profile_me


urlpatterns = [
	url(r'^info/$', member_profile_all, name='profile_info_all'),
	url(r'^info/me/$', member_profile_me, name='profile_info_me'),
	url(r'^info/(?P<pk>\d+)/$', member_profile, name='profile_info'),  #todo: use slug instead of id
	url(r'^info/(?P<pk>\d+)-(?P<label>[-\w]+)/$', member_profile, name='profile_info'),
	url(r'^login_register/$', lambda request: None, name='profile_settings'),  # todo: already implemented? -> hard to implement (handle incorrect credentials)
]


