
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from functools import lru_cache
from re import findall
from base.admin import census_admin
from base.admin import superuser_admin
from .models import Member, Team


class SystemMemberAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Personal', {'fields': ('first_name', 'last_name',)}),
		('Contact', {'fields': ('email',)}),
		('Technical', {'fields': ('is_active', 'last_login', 'date_joined',)}),
	)
	readonly_fields = ('last_login', 'date_joined',)
	list_display = ('username', 'first_name', 'last_name', 'is_active',)
	list_filter = ('is_active', 'last_login', 'date_joined',)
	search_fields = ('username', 'first_name', 'last_name',)
	list_display_links = ('username', 'first_name', 'last_name',)
	ordering = ('username',)
	#filter_horizontal = ('teams',) #todo replace with groups
	show_full_result_count = True
	view_on_site = True
	#todo: show groups as readonly attribute


class TechnicalMemberAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Contact', {'fields': ('get_full_name', 'email',)}),
		('Technical', {'fields': ('is_active', 'last_login', 'date_joined',)}),
	)
	readonly_fields = ('last_login', 'date_joined', 'email', 'get_full_name',)
	list_display = ('username', 'get_full_name', 'is_active', 'last_login', 'date_joined',)
	list_filter = ('is_active', 'last_login', 'date_joined',)
	search_fields = ('username', 'first_name', 'last_name',)
	list_display_links = ('username', 'get_full_name',)
	ordering = ('username',)
	#filter_horizontal = ('teams',) #todo replace with groups
	show_full_result_count = True
	view_on_site = True
	#todo: fully show editable groups


census_admin.register(Member, SystemMemberAdmin)
superuser_admin.register(Member, TechnicalMemberAdmin)

#
# @lru_cache(maxsize = 256)
# def _get_team_system(url):
# 	"""
# 	Get the current team from the url, and find out if it's a system team.
#
# 	Use caching for efficiency (less inefficiency). Team system status should be fixed anyway.
#
# 	This is very hack-ish and terrible, but it seems like Django is intentionally making this difficult.
# 	"""
# 	pk = int(findall(
# 		r'/{0:s}/{1:s}/(\d+)/'.format(Team._meta.app_label.lower(), Team._meta.object_name.lower()),
# 		'{0:s}/'.format(url),  # in case APPEND_SLASH is off
# 	)[0])
# 	team = Team.objects.get(pk = pk)
# 	return team.system
#
#
"""
class TeamMemberInline(admin.TabularInline):
	model = TeamMember
	verbose_name = 'team member'
	extra = 1

	def get_readonly_fields(self, request, obj = None):
		if obj is None:
			return []
		if obj.system:
			return ['member', 'team', 'admin', 'role']
		return []

	def has_add_permission(self, request, obj = None):
		return not _get_team_system(request.get_full_path())

	def has_delete_permission(self, request, obj = None):
		return not _get_team_system(request.get_full_path())
	# 	for f in dir(self):
	# 		print(f)
	# 	print('get_add', obj)
	# 	return False
	# 	print('get_add', obj)
	# 	return not self.instance.system
	#
	# #def has_change_permission(self, request, obj = None):
	# #	return not self.instance.system
	#
	# def has_delete_permission(self, request, obj = None):
	# 	print('get_del', obj)
	# 	return False
	# 	print('get_del', obj)
	# 	return not self.instance.system
"""

#name = models.CharField(max_length = 48, unique = True, error_messages = {'unique': 'A team with that name already exists.'})
# slug = AutoSlugField(populate_from='name', unique=True, help_text='This value is used as identifier in places like urls.')
# listed = models.BooleanField(default=False)
# description = models.TextField(default='', blank=True)
# system = models.BooleanField(default=False)
# # members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, through='teams.TeamMember')



class SystemTeamAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {'fields': ('name',)}),
		('Information', {'fields': ('description', 'listed', 'slug',)}),
		('Information', {'fields': ('member_count', 'user',)}),
		('Permissions', {'fields': ('permission_census', 'permission_superuser', 'system',)}),
	)
	readonly_fields = ('system', 'member_count', 'slug',)
	list_display = ('name', 'member_count', 'listed', 'permission_census', 'permission_superuser', 'system',)
	list_filter = ('listed', 'permission_census', 'permission_superuser', 'system',)
	search_fields = ('name', 'slug', 'description',)
	ordering = ('name',)
	filter_horizontal = tuple()
	show_full_result_count = True
	view_on_site = True

	def save_model(self, request, obj, form, change):
		if obj.system and not request.user.is_superuser:
			raise PermissionError('You cannot change system groups unless you are a superuser.')
		super().save_model(request=request, obj=obj, form=form, change=change)

	# def __init__(self, *args, **kwargs):
	# 	super(FullTeamAdmin, self).__init__(*args, **kwargs)
	# 	print(self)
	# 	print(args)
	# 	print(kwargs)


	#todo: member administration
	#inlines = (TeamMemberInline,)

	#def get_readonly_fields(self, request, obj = None):
	#	if obj.system:
	#		return ['member', 'team', 'admin', 'role']
	#	return []


class CensusTeamAdmin(SystemTeamAdmin):
	readonly_fields = SystemTeamAdmin.readonly_fields + ('permission_superuser',)

	# todo: member administration
	# inlines = (TeamMemberInline,)


census_admin.register(Team, CensusTeamAdmin)
superuser_admin.register(Team, SystemTeamAdmin)

# """ Remove Site here because this app is one of the last to be loaded, as opposed to ctrl. """
# admin.site.unregister(Site)

#
#
# from django.contrib.admin import site
# from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
# from member.models import Member
#
#
# class MemberAdmin(UserAdmin):
# 	fieldsets = (
# 		(None, {'fields': ('username', 'password')}),
# 		(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
# 		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
# 		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
# 	)
# 	#todo: add teams back in some way?
#
#
# site.register(Member, MemberAdmin)
#
#
