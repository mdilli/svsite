
from allauth.account.models import EmailAddress
from allauth.account.models import EmailConfirmation
from allauth.socialaccount.models import SocialApp, SocialToken, SocialAccount
from allauth.socialaccount.providers.openid.admin import OpenIDNonceAdmin
from allauth.socialaccount.providers.openid.admin import OpenIDStoreAdmin
from allauth.socialaccount.providers.openid.models import OpenIDNonce, OpenIDStore
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.db import models
from django.forms import ModelForm, ModelMultipleChoiceField
from ordered_model.admin import OrderedTabularInline
from base.admin import census_admin, content_admin
from base.admin import superuser_admin
from .models import Member, Team, TeamRole, TeamAdmin
from allauth.account.admin import EmailAddressAdmin, EmailConfirmationAdmin
from allauth.socialaccount.admin import SocialAccountAdmin, SocialTokenAdmin, SocialAppAdmin


class SystemMemberAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Personal', {'fields': ('first_name', 'last_name',)}),
		('Contact', {'fields': ('email',)}),
		('Technical', {'fields': ('is_active', 'last_login', 'date_joined', 'theme',)}),
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


class TeamAdminAdmin(admin.TabularInline):
	model = TeamAdmin
	# list_display = ('team', 'member',)
	fields = ('member',)
	extra = 1


class TeamRoleAdmin(OrderedTabularInline):
	model = TeamRole
	# list_display = ('team', 'member', 'role',)
	fields = ('move_up_down_links', 'member', 'title', 'order',)
	readonly_fields = ('order', 'move_up_down_links',)
	formfield_overrides = {models.TextField: {'widget': forms.TextInput},}
	ordering = ('order',)
	extra = 1


class SystemTeamAdmin(admin.ModelAdmin):
	form = TeamAdminForm
	fieldsets = (
		(None, {'fields': ('name',)}),
		('Information', {'fields': ('description', 'listed', 'slug', 'member_count',)}),
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
	inlines = (TeamAdminAdmin, TeamRoleAdmin,)

	def save_model(self, request, obj, form, change):
		if obj.system and not request.user.is_superuser:
			raise PermissionError('You cannot change system groups unless you are a superuser.')
		super().save_model(request=request, obj=obj, form=form, change=change)

	def get_urls(self):
		return self.inlines[1].get_urls(model_admin=self) + \
			super().get_urls()


class CensusTeamAdmin(SystemTeamAdmin):
	readonly_fields = SystemTeamAdmin.readonly_fields + ('permission_superuser',)


census_admin.register(Team, CensusTeamAdmin)
superuser_admin.register(Team, SystemTeamAdmin)

content_admin.unregister(Group)
content_admin.unregister(EmailAddress)
content_admin.unregister(EmailConfirmation)
content_admin.unregister(SocialApp)
content_admin.unregister(SocialToken)
content_admin.unregister(SocialAccount)
content_admin.unregister(OpenIDNonce)
content_admin.unregister(OpenIDStore)
census_admin.register(EmailAddress, EmailAddressAdmin)
census_admin.register(EmailConfirmation, EmailConfirmationAdmin)
census_admin.register(SocialApp, SocialAppAdmin)
census_admin.register(SocialToken, SocialTokenAdmin)
census_admin.register(SocialAccount, SocialAccountAdmin)
census_admin.register(OpenIDNonce, OpenIDNonceAdmin)
census_admin.register(OpenIDStore, OpenIDStoreAdmin)


