
from django.conf.urls import url
from badges.views import badge_win, badge_info


urlpatterns = (
	url(r'^win/$', badge_win, name='win'),
	url(r'^info/', badge_info),
)


