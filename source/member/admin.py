
from django.contrib.auth.admin import UserAdmin
from .models import Member
from svsite.admin import census_admin
from svsite.admin import superuser_admin


class FullMemberAdmin(UserAdmin):
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
	filter_horizontal = ('teams',)
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
	filter_horizontal = ('teams',)
	show_full_result_count = True
	view_on_site = True
	#todo: fully show editable groups


census_admin.register(Member, FullMemberAdmin)
superuser_admin.register(Member, TechnicalMemberAdmin)


