
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Team(Group):
	listed = models.BooleanField(default = False)
	description = models.TextField(default = '', blank = True)

	class Meta:
		verbose_name = _('Team')
		verbose_name_plural = _('Teams')

	def get_absolute_url(self):
		return reverse('group_info', kwargs = {'pk': self.pk, 'label': slugify(self.name)})  #todo


class TeamMember(models.Model):
	member = models.ForeignKey('member.Member')
	team = models.ForeignKey('teams.Team')
	admin = models.BooleanField(default = False, help_text = _('Admins can and and remove members and update descriptions'))


