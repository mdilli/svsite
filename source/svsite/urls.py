"""
svsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.views import static
import grappelli.urls
import allauth.urls
import census.urls
import member.urls
import activity.urls
import cms.urls
from svsite.backups import download_database, upload_database

try:
	from svsite.playground import playground
except ImportError:
	playground = lambda request: HttpResponse('nothing here')


urlpatterns = i18n_patterns('',
	url(r'^$', lambda request: HttpResponse('under construction')),
	url(r'^test/$', playground),
	url(r'^grappelli/', include(grappelli.urls)),
	url(r'^admin/backup/', download_database, name = 'backup'),
	url(r'^admin/restore/', upload_database, name = 'restore'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^user/', include(allauth.urls)),
	url(r'^census/', include(census.urls)),
	url(r'^user/', include(member.urls)),
	url(r'^event/', include(activity.urls)),
	url(r'^c/', include(cms.urls)),
	#todo: if cms keeps it's prefix, make a redirect for leftover urls to that prefix
)


if settings.DEBUG:
	urlpatterns = patterns('',
		url(r'^{0:s}/(?P<path>.*)$'.format(settings.MEDIA_URL.strip('/')), static.serve,
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
		) + staticfiles_urlpatterns() + urlpatterns


