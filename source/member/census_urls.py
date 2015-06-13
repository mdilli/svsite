
from django.conf.urls import url
from census.admin import census_admin


urlpatterns = [
	url(r'^$', census_admin.urls, name = 'census_overview'),
	#url(r'^(?P<pk>\d+)/$', member_profile, name = 'member_profile'),
]


