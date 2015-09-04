from django.contrib.auth.models import Group, Permission, GroupManager
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django_extensions.db.fields import AutoSlugField

from ctrl.models import GroupPermissionMixin


class Team(GroupPermissionMixin):
	name = models.CharField(max_length = 48, unique = True, error_messages = {'unique': 'A team with that name already exists.'})
	slug = AutoSlugField(populate_from = 'name', unique = True)
	listed = models.BooleanField(default = False)
	description = models.TextField(default = '', blank = True)
	members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True, through = 'teams.TeamMember')

	objects = GroupManager()

	class Meta:
		verbose_name = _('Team')
		verbose_name_plural = _('Teams')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# todo
		return reverse('group_info', kwargs = {'pk': self.pk, 'label': slugify(self.name)})

	def natural_key(self):
		return (self.name,)


class TeamMember(models.Model):
	member = models.ForeignKey(settings.AUTH_USER_MODEL)
	team = models.ForeignKey('teams.Team')
	admin = models.BooleanField(default = False, help_text = 'Admins can and and remove members and update descriptions')
	role = models.CharField(max_length = 64, blank = True, default = '')

	class Meta:
		unique_together = ('member', 'team',)

	def __str__(self):
		return '{0:} ∈ {1:}'.format(self.member, self.team)


