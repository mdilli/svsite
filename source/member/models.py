
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django_extensions.db.fields import AutoSlugField
from ctrl.models import UserPermissionManager


class Member(AbstractUser):
	slug = AutoSlugField(populate_from='username', unique=True)
	#teams = models.ManyToManyField('teams.Team', blank=True, through='teams.TeamMember')
	birthday = models.DateField(blank=True, null=True, default=None)

	objects = UserPermissionManager()

	# class Meta:
	# 	abstract = False
	# 	app_label = 'member'

	def __str__(self):
		return self.get_full_name()

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip() or self.username

	def get_short_name(self):
		return self.first_name or self.username

	def get_absolute_url(self):
		return '/'  # todo


