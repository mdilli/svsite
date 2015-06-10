
from django.conf.urls import url
from activity.views import to_activity_overview, ActivityOverview, ActivityInfo


urlpatterns = [
	url(r'^$', to_activity_overview),
	url(r'^all/$', ActivityOverview.as_view(), name = 'activity_overview'),
	url(r'^(?P<pk>\d+)/$', ActivityInfo.as_view(), name = 'activity_info'),
	url(r'^(?P<pk>\d+)-(?P<label>[-\w]+)/$', ActivityInfo.as_view(), name = 'activity_info'),
]


