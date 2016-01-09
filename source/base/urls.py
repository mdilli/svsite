
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import static
from misc.forms.search import SearchForm
from misc.views.autocomplete import autocomplete
from misc.views.db_backups import download_media, download_database, upload_database
from ctrl.admin import superuser_admin
from ctrl.admin import census_admin
from haystack.views import SearchView
import allauth.urls
import cms.urls
import member.urls
import activity.urls

try:
	from base.playground import playground
except ImportError:
	playground=lambda request: HttpResponse('nothing here')


urlpatterns=i18n_patterns('',
	#url(r'^$', lambda request: HttpResponse('under construction'), name='home'),
	url(r'^$', lambda request: redirect('c/'), name='home'),
	url(r'^contact$', lambda request: HttpResponse('under construction'), name='contact'),
	url(r'^test$', playground),
	url(r'^admin/?', lambda request: redirect(reverse('admin:index'))),
	url(r'^\$/', include(admin.site.urls)),
	url(r'^user/', include(allauth.urls)),
#	url(r'^su/backup', download_database, name='backup'),
#	url(r'^su/restore', upload_database, name='restore'),
	url(r'^su/', superuser_admin.urls, name='superuser_admin'),
	url(r'^census/', census_admin.urls, name='census_admin'),
	url(r'^user/', include(member.urls)),
	url(r'^event/', include(activity.urls)),
	# misc
	url(r'^su/', include(admin.site.urls)),
	url(r'^su/backup/media$', download_media, name='backup_media'),
	url(r'^su/backup/db$', download_database, name='backup_db'),
	url(r'^su/backup$', lambda request: redirect(reverse('backup_db')), name='backup'),
	url(r'^su/restore$', upload_database, name='restore'),
	url(r'^search$', SearchView(template='search_page.html', form_class=SearchForm), name='search'),
	url(r'^autocomplete$', autocomplete, name='autocomplete'),
	# cms
	url(r'^c/', include(cms.urls)),   # last
	# todo: if cms keeps it's prefix, make a redirect for leftover urls to that prefix
)


if settings.DEBUG:
	urlpatterns=patterns('',
		url(r'^{0:s}/(?P<path>.*)$'.format(settings.MEDIA_URL.strip('/')), static.serve,
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
		) + staticfiles_urlpatterns() + urlpatterns


