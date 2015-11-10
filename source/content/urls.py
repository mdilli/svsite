
from cms.sitemaps import CMSSitemap
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),  #todo: unused?
    url(r'^select2/', include('django_select2.urls')), #todo: what is this?
    url(r'^', include('cms.urls')),
)


