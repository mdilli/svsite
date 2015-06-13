
from django.conf.urls import url
from member.admin import census_admin


urlpatterns = [
	url(r'^$', census_admin.urls, name = 'census_overview'),
]


