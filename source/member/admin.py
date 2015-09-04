
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
		return super().has_permission(request)  # and has_perm('member.')


census_admin = CensusAdminSite(name = 'census')


@admin.register(Member)
class MemberAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		# ('Study', {'fields': ('biology', 'chemistry', 'physics_astronomy', 'computing_science', 'molecular_life_science', 'mathematics', 'science', 'progress', 'specialization',)}),
		('Technical', {'fields': ('is_active', 'is_staff', 'last_login', 'date_joined',)}),
	)
	readonly_fields = ('last_login', 'date_joined',)
	list_display = ('username', 'is_active', 'is_staff', 'last_login', 'date_joined',)
	list_filter = ('is_active', 'is_staff', 'last_login', 'date_joined',)
	search_fields = ('username',)
	ordering = ('last_login', 'date_joined',)
	filter_horizontal = ('groups',)
	show_full_result_count = True
	view_on_site = True


census_admin.register(Member, MemberAdmin)
admin.site.register(Permission)
admin.site.unregister(Permission)


