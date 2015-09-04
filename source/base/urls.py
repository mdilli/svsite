
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse, HttpResponseRedirect
from django.views import static
from ctrl.admin import superuser_admin
from ctrl.admin import census_admin
from ctrl.backups import download_database, upload_database
import allauth.urls
import cms.urls
import member.urls
import activity.urls

try:
	from base.playground import playground
except ImportError:
	playground = lambda request: HttpResponse('nothing here')


urlpatterns = i18n_patterns('',
	#url(r'^$', lambda request: HttpResponse('under construction'), name = 'home'),
	url(r'^$', lambda request: HttpResponseRedirect('c/'), name = 'home'),
	url(r'^contact/$', lambda request: HttpResponse('under construction'), name = 'contact'),
	url(r'^test/$', playground),
	url(r'^admin/', lambda request: HttpResponseRedirect('/su/')),
	url(r'^user/', include(allauth.urls)),
    url(r'^su/backup/', download_database, name = 'backup'),
    url(r'^su/restore/', upload_database, name = 'restore'),
	url(r'^su/', superuser_admin.urls, name = 'superuser_admin'),
    url(r'^census/', census_admin.urls, name = 'census_admin'),
	url(r'^user/', include(member.urls)),
	url(r'^event/', include(activity.urls)),
	url(r'^c/', include(cms.urls)),
	# todo: if cms keeps it's prefix, make a redirect for leftover urls to that prefix
)


if settings.DEBUG:
	urlpatterns = patterns('',
		url(r'^{0:s}/(?P<path>.*)$'.format(settings.MEDIA_URL.strip('/')), static.serve,
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
		) + staticfiles_urlpatterns() + urlpatterns


