
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm, ModelMultipleChoiceField
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
	list_filter = ('is_active',)
	search_fields = ('username', 'first_name', 'last_name',)
	list_display_links = ('username', 'first_name', 'last_name',)
	ordering = ('username',)
	show_full_result_count = True
	view_on_site = True


class TechnicalMemberAdmin(SystemMemberAdmin):
	readonly_fields = SystemMemberAdmin.readonly_fields + ('email', 'get_full_name',)
	list_display = SystemMemberAdmin.list_display + ('last_login', 'date_joined',)
	list_filter = SystemMemberAdmin.list_filter + ('last_login', 'date_joined',)


census_admin.register(Member, SystemMemberAdmin)
superuser_admin.register(Member, TechnicalMemberAdmin)


class TeamAdminForm(ModelForm):
	users = ModelMultipleChoiceField(Member.objects.filter(is_active=True), required=False,
		 widget=admin.widgets.FilteredSelectMultiple('Member', False))

	def __init__(self, *args, **kwargs):
		super(TeamAdminForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.initial['users'] = self.instance.user_set.values_list('pk', flat=True)

	def save(self, *args, **kwargs):
		instance = super(TeamAdminForm, self).save(*args, **kwargs)
		if instance.pk:
			instance.user_set.clear()
			instance.user_set.add(*self.cleaned_data['users'])
		return instance


class SystemTeamAdmin(admin.ModelAdmin):
	form = TeamAdminForm
	fieldsets = (
		(None, {'fields': ('name',)}),
		('Information', {'fields': ('description', 'listed', 'slug',)}),
		('Information', {'fields': ('member_count', 'users',)}),
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


class CensusTeamAdmin(SystemTeamAdmin):
	readonly_fields = SystemTeamAdmin.readonly_fields + ('permission_superuser',)


census_admin.register(Team, CensusTeamAdmin)
superuser_admin.register(Team, SystemTeamAdmin)


