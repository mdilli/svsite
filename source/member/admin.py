
"""
	Create a second admin website for members, and register member models.

	Second admin: https://stackoverflow.com/questions/3206856/how-to-have-2-different-admin-sites-in-a-django-project
"""

from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from .models import Member


class CensusAdminSite(AdminSite):

	site_header = 'Census member administration'
	site_title = site_header
	site_url = '/'
	index_title = site_header

	def has_permission(self, request):
		#todo: create a special permission for viewing census admin (but permissions in migrations are tricky)
		return super().has_permission(request)# and has_perm('member.')


census_admin = CensusAdminSite(name = 'census')


census_admin.register(Member, UserAdmin)
admin.site.register(Member, UserAdmin)
admin.site.register(Permission)


