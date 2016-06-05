
from cms.sitemaps import CMSSitemap
from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
import minimal_logger.urls
from base.views import playground


urlpatterns = (
	url(r'^playground/$', playground),
	url(r'^log/', include(minimal_logger.urls)),
	url(r'^sitemap.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),  # todo: do something to have this used?
	# url(r'^backup/media$', download_media, name='backup_media'),
	# url(r'^backup/db$', download_database, name='backup_db'),
	# url(r'^backup$', lambda request: redirect(reverse('backup_db')), name='backup'),
	# url(r'^backup/restore$', upload_database, name='restore'),
)


