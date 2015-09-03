from cms.admin.useradmin import PageUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from member.admin import census_admin
from teams.models import Team, TeamMember


PageUserAdmin

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	"""
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Study', {'fields': ('biology', 'chemistry', 'physics_astronomy', 'computing_science', 'molecular_life_science', 'mathematics', 'science', 'progress', 'specialization',)}),
		('Technical', {'fields': ('is_active', 'is_staff', 'last_login', 'date_joined',)}),
	)
	readonly_fields = ('last_login', 'date_joined',)
	list_display = ('username', 'is_active', 'is_staff', 'last_login', 'date_joined', 'study_info',)
	list_filter = ('is_active', 'is_staff', 'last_login', 'date_joined', 'progress', 'biology', 'chemistry', 'physics_astronomy', 'computing_science', 'molecular_life_science', 'mathematics', 'science',)
	search_fields = ('username',)
	ordering = ('last_login', 'date_joined',)
	filter_horizontal = tuple()
	show_full_result_count = True
	view_on_site = True
	"""
	def formfield_for_manytomany(self, db_field, request=None, **kwargs):
		if db_field.name == 'permissions':
			qs = kwargs.get('queryset', db_field.rel.to.objects)
			# Avoid a major performance hit resolving permission names which
			# triggers a content_type load:
			kwargs['queryset'] = qs.select_related('content_type')
		return super(TeamAdmin, self).formfield_for_manytomany(
			db_field, request=request, **kwargs)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
	"""
	list_display = ('given_by', 'used_by', 'created', 'is_expired',)
	list_filter = ('created',)
	search_fields = ('given_by__username', 'used_by__username',)
	ordering = ('created',)
	"""


census_admin.register(Team, TeamAdmin)
census_admin.register(TeamMember, TeamMemberAdmin)
admin.site.unregister(Group)


