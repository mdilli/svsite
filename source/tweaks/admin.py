
from cms.admin.useradmin import PageUserGroupAdmin
from cms.models import PageUser, PageUserGroup
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin
from base.admin import content_admin, superuser_admin, census_admin


content_admin.unregister(PageUser)  #todo: might be a problem?
content_admin.unregister(PageUserGroup)  #todo: might be a problem?
census_admin.register(PageUserGroup, PageUserGroupAdmin)
superuser_admin.register(PageUserGroup, PageUserGroupAdmin)
content_admin.unregister(Site)
superuser_admin.register(Site, SiteAdmin)


