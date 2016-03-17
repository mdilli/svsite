
from django.conf import settings
from django.contrib.auth.models import Group, UserManager, AbstractUser, GroupManager
from django.core.urlresolvers import reverse
from django.db.models.signals import m2m_changed, post_save
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from django.db import models
from sortedm2m.fields import SortedManyToManyField


class Member(AbstractUser):

	slug = AutoSlugField(populate_from='username', unique=True)
	birthday = models.DateField(blank=True, null=True, default=None)

	objects = UserManager()

	@property
	def teams(self):
		return Team.objects.filter(user=self)

	def listed_teams(self):
		return Team.objects.filter(user=self, listed=True)

	def __str__(self):
		return self.get_full_name()

	def get_full_name(self):
		full_name = '{0:s} {1:s}'.format(self.first_name, self.last_name)
		return full_name.strip() or self.username.title()

	def get_short_name(self):
		return self.first_name or self.username.title()

	def get_absolute_url(self):
		return reverse('profile_info', kwargs=dict(pk=self.pk, label=self.slug))

	def has_permission_superuser(self):
		return True  # todo

	def has_permission_census(self):
		return True  # todo


class Team(Group):
	slug = AutoSlugField(populate_from='name', unique=True, help_text='This value is used as identifier in places like urls.')
	listed = models.BooleanField(default=False)
	description = models.TextField(default='', blank=True)
	permission_census = models.BooleanField(default=False)
	permission_superuser = models.BooleanField(default=False)
	system = models.BooleanField(default=False)
	admins = models.ManyToManyField(settings.AUTH_USER_MODEL, through='member.TeamAdmin', related_name='admin_teams')
	roles = SortedManyToManyField(settings.AUTH_USER_MODEL, through='member.TeamRole', related_name='team_roles')

	objects = GroupManager()

	class Meta:
		verbose_name = _('Team')
		verbose_name_plural = _('Teams')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return '/'  # todo
		# return reverse('group_info', kwargs = {'pk': self.pk, 'label': slugify(self.name)})

	def natural_key(self):
		return (self.slug,)

	def member_count(self):
		return self.user_set.count()


class TeamMemberBase(models.Model):
	member = models.ForeignKey(settings.AUTH_USER_MODEL)
	team = models.ForeignKey('member.Team')
	# group = models.ForeignKey('auth.Group')

	class Meta:
		unique_together = ('member', 'team',)
		abstract = True

	def __str__(self):
		return '{0:} A∈ {1:}'.format(self.member, self.team)


class TeamAdmin(TeamMemberBase):
	pass


class TeamRole(TeamMemberBase):
	# group = models.ForeignKey('auth.Group')
	# is_active = models.BooleanField(default=False, help_text='Admins can and and remove members and update details.')
	# is_member = models.BooleanField(default=True, help_text='Admins can and and remove members and update details.')
	role = models.TextField(blank=True, default='')


def mirror_members(*args, **kwargs):
	print('*** MIRRORING MEMBERS ***')
	print(args, kwargs)
	return
	if action == 'post_clear':
		pass
	if action == 'post_add':
		pass
	print('MIRRORING MEMBERS')
	group = instance
	# groups = reverse
	print('instance', instance)
	print('reverse', reverse)
	print('sender', sender)
	print('pk_set', pk_set)
	print('action', action)
	print('signal', signal)
	print('model', model)
	print('using', using)


#m2m_changed.connect(mirror_members, sender=Team.roles.through)
post_save.connect(mirror_members, sender=TeamRole)


