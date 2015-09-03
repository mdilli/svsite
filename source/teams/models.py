
from django.contrib.auth.models import Group, Permission, GroupManager
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Team(models.Model):
	name = models.SlugField(unique = True, error_messages = {'unique':'A user with that username already exists.'})
	listed = models.BooleanField(default = False)
	description = models.TextField(default = '', blank = True)
	members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True, through = 'teams.TeamMember')

	permissions = models.ManyToManyField(Permission, blank = True)

	objects = GroupManager()

	class Meta:
		verbose_name = _('Team')
		verbose_name_plural = _('Teams')

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('group_info', kwargs = {'pk': self.pk, 'label': slugify(self.name)})  #todo

	def natural_key(self):
		return (self.name,)


class TeamMember(models.Model):
	member = models.ForeignKey(settings.AUTH_USER_MODEL)
	team = models.ForeignKey('teams.Team')
	admin = models.BooleanField(default = False, help_text = _('Admins can and and remove members and update descriptions'))
	role = models.CharField(max_length = 64, blank = True, default = '')


# def user_team_update(sender, **kwargs):
# 	print('update!', sender, kwargs)
#
# models.signals.m2m_changed.connect(user_team_update, sender = TeamMember)


