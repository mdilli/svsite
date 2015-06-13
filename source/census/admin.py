
"""
	Create a second admin website for members.

	See https://stackoverflow.com/questions/3206856/how-to-have-2-different-admin-sites-in-a-django-project
"""

from django.contrib.admin.sites import AdminSite


class CensusAdminSite(AdminSite):
	pass


census_admin = CensusAdminSite()


