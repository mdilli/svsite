
"""
	Create a second admin website for members, and register member models.

	Second admin: https://stackoverflow.com/questions/3206856/how-to-have-2-different-admin-sites-in-a-django-project
"""

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy as _
# from base.models import SearchResults


# class MultilingualModelAdmin(TranslatableAdmin, PlaceholderAdminMixin, admin.ModelAdmin):
# 	pass


# admin.site.register(SearchResults, MultilingualModelAdmin)


class SuperuserAdminSite(AdminSite):

	site_header = _('Superuser administration')
	site_title = site_header
	site_url = '/'
	index_title = site_header

	def has_permission(self, request):
		if not request.user.is_active:
			return False
		return request.user.has_permission_superuser


class CensusAdminSite(AdminSite):

	site_header = _('Member administration')
	site_title = site_header
	site_url = '/'
	index_title = site_header

	def has_permission(self, request):
		if not request.user.is_active:
			return False
		return request.user.has_permission_census


superuser_admin = SuperuserAdminSite(name='superuser')
census_admin = CensusAdminSite(name='census')
content_admin = admin.site
content_admin.site_header = content_admin.site_title = _('Content administration')


