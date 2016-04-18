
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
import filer.urls
import cms.urls
import badges.urls
import allauth.urls
import member.member_urls, member.team_urls
import birthdays.urls
import base.urls
import searcher.urls
import svfinance.urls
import intapi.urls
from base.admin import superuser_admin, census_admin
from base.views import playground


urlpatterns = i18n_patterns(
	url(r'^€/', include(svfinance.urls)),
	url(r'^\$playground', playground),
	url(r'^member/', include(member.member_urls)),
	url(r'^cie/', include(member.team_urls)),
	url(r'^account/', include(allauth.urls)),
	url(r'^badge/', include(badges.urls)),
	url(r'^search/', include(searcher.urls)),
	url(r'^birthday/', include(birthdays.urls)), #todo
	url(r'^\$content/', include(admin.site.urls)),
	url(r'^\$sudo/', include(superuser_admin.urls)),
	url(r'^\$members/', include(census_admin.urls)),
	url(r'^filer/', include(filer.urls)),   # django filer canonical urls (ones that don't change if you upload a new version)
	url(r'^', include(base.urls)),
	url(r'^', include(cms.urls)),
) + \
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
[
	url(r'^\$intapi/', include(intapi.urls)),
]


