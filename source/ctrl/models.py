
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.apps import apps


class GroupPermissionMixin(models.Model):

	permission_census = models.BooleanField(default = False)
	permission_superuser = models.BooleanField(default = False)

	class Meta:
		abstract = True


class UserPermissionMixin():

	@property
	def has_permission_census(self):
		"""
			Check if the user has access to the census admin. There is only one permission, you can do everything or nothing.
		"""
		for team in self.teams.all():
			if team.permission_census:
				return True
		return False

	@property
	def has_permission_superuser(self):
		"""
			Similar to has_permission_census .
		"""
		for team in self.teams.all():
			if team.permission_superuser:
				return True
		return False

	def has_perm(self, perm, obj=None):
		"""
			Everyone (active) has every permission, but access to the admin site is regulated by their groups.
		"""
		#todo: this is probably not secure (fake post requests)
		#todo: maybe defer to has_module_perms
		return self.is_active

	def has_module_perms(self, app_label):
		"""
			See has_perm
		"""
		#todo: like has_perm
		return self.is_active


class UserPermissionManager(UserManager):

	def create_superuser(self, username, email, password, **extra_fields):
		"""
			Create admins group with superuser powers.
		"""
		Team = apps.get_model(app_label = 'teams', model_name = 'Team')
		TeamMember = apps.get_model(app_label = 'teams', model_name = 'TeamMember')
		user = super(UserPermissionManager, self).create_superuser(username, email, password, **extra_fields)
		try:
			team = Team.objects.get(name = 'Admins')
		except Team.DoesNotExist:
			team = Team(name = 'admins', permission_superuser = True, permission_census = True)
			print('created "admins" group')
			team.save()
		tm = TeamMember(member = user, team = team, admin = True)
		tm.save()
		return user


