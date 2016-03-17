
from cms.models import PageUser
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin
from base.admin import content_admin, superuser_admin


def shrink_cms_admin():
	content_admin.unregister(PageUser)


content_admin.unregister(Site)
superuser_admin.register(Site, SiteAdmin)


