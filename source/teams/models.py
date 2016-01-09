
from django.contrib.auth.models import GroupManager, Group
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import m2m_changed
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from ctrl.models import GroupPermissionMixin
from member.models import Member


if not hasattr(Group, 'parent'):
	AutoSlugField(populate_from='name', unique=True, help_text='This value is used as identifier in places like urls.')\
		.contribute_to_class(Group, 'slug')
	models.BooleanField(default=False)\
		.contribute_to_class(Group, 'listed')
	models.TextField(default='', blank=True)\
		.contribute_to_class(Group, 'description')
	models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, through='teams.TeamRole')\
		.contribute_to_class(Member, 'teams')


def mirror_teams_groups(sender, instance, action, reverse, model, pk_set, **kwargs):
	# http://stackoverflow.com/questions/4744794/django-cannot-detect-changes-on-many-to-many-field-with-m2m-changed-signal-au
	if action == 'post_add':
		print('add', pk_set)
	#todo: is this a good idea?


m2m_changed.connect(mirror_teams_groups, sender=Member.groups.through)


class Team(Group):
	"""
		Proxy model extending group: http://stackoverflow.com/questions/2181039/how-do-i-extend-the-django-group-model
	"""
	#name = models.CharField(max_length = 48, unique = True, error_messages = {'unique': 'A team with that name already exists.'})
	#slug = AutoSlugField(populate_from='name', unique=True, help_text='This value is used as identifier in places like urls.')
	#listed = models.BooleanField(default=False)
	#description = models.TextField(default='', blank=True)
	#members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, through='teams.TeamMember')

	objects = GroupManager()

	class Meta:
		proxy = True
		verbose_name = _('Team')
		verbose_name_plural = _('Teams')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# todo
		return reverse('group_info', kwargs = {'pk': self.pk, 'label': slugify(self.name)})

	def natural_key(self):
		return (self.slug,)

	def member_count(self):
		return self.members.count()



class TeamRole(models.Model):
	member = models.ForeignKey(settings.AUTH_USER_MODEL)
	#team = models.ForeignKey('teams.Team')
	group = models.ForeignKey('auth.Group')
	admin = models.BooleanField(default=False, help_text='Admins can and and remove members and update descriptions')
	role = models.CharField(max_length=64, blank=True, default='')

	class Meta:
		unique_together = ('member', 'group',)

	def __str__(self):
		return '{0:} ∈ {1:}'.format(self.member, self.team)


