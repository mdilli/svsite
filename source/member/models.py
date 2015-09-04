from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.fields import AutoSlugField

from ctrl.models import UserPermissionMixin, UserPermissionManager
from teams.models import Team, TeamMember


class Member(AbstractUser, UserPermissionMixin):
	slug = AutoSlugField(populate_from = 'username', unique = True)
	teams = models.ManyToManyField('teams.Team', blank = True, through = 'teams.TeamMember')

	objects = UserPermissionManager()

	def __str__(self):
		return self.get_full_name()

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip() or self.username

	def get_short_name(self):
		return self.first_name or self.username

	def get_absolute_url(self):
		return '/'  # todo


