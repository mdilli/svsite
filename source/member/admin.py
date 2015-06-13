
"""
	Create a second admin website for members, and register member models.

	Second admin: https://stackoverflow.com/questions/3206856/how-to-have-2-different-admin-sites-in-a-django-project
"""

from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import svUser


class CensusAdminSite(AdminSite):
	pass


census_admin = CensusAdminSite()


census_admin.register(svUser, UserAdmin)
admin.site.register(svUser, UserAdmin)


