
from django.conf import settings
from django.contrib.auth.models import Group, UserManager, AbstractUser, GroupManager
from django.core.urlresolvers import reverse
from django.db.models.signals import m2m_changed, post_save, post_delete
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from django.db import models
from ordered_model.models import OrderedModel


class Member(AbstractUser):
	slug = AutoSlugField(populate_from='username', unique=True)
	birthday = models.DateField(blank=True, null=True, default=None)
	# note: do NOT change groups directly, use Team.roles instead

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

	@property
	def role_throughs(self):
		return TeamRole.objects.filter(member=self)


class Team(Group):
	slug = AutoSlugField(populate_from='name', unique=True, help_text='This value is used as identifier in places like urls.')
	listed = models.BooleanField(default=False)
	description = models.TextField(default='', blank=True)
	permission_census = models.BooleanField(default=False)
	permission_superuser = models.BooleanField(default=False)
	system = models.BooleanField(default=False)
	admins = models.ManyToManyField(settings.AUTH_USER_MODEL, through='member.TeamAdmin', related_name='admin_teams')
	roles = models.ManyToManyField(settings.AUTH_USER_MODEL, through='member.TeamRole', related_name='team_roles')


	objects = GroupManager()

	class Meta:
		verbose_name = _('Team')
		verbose_name_plural = _('Teams')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('team_info', kwargs=dict(slug=self.slug))

	def natural_key(self):
		return (self.slug,)

	def member_count(self):
		return self.user_set.count()

	@property
	def role_throughs(self):
		return TeamRole.objects.filter(team=self)


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


class TeamRole(OrderedModel, TeamMemberBase):
	# group = models.ForeignKey('auth.Group')
	# is_active = models.BooleanField(default=False, help_text='Admins can and and remove members and update details.')
	# is_member = models.BooleanField(default=True, help_text='Admins can and and remove members and update details.')
	title = models.TextField(blank=True, default='')
	# order = models.IntegerField(default=0, unique=True)

	order_with_respect_to = 'team'

	class Meta(OrderedModel.Meta, TeamMemberBase.Meta):
		pass


def mirror_members(signal, using, sender, instance, **kwargs):
	#todo: may be faster to attach to m2m_changed
	roles = instance.team.roles.all()
	instance.team.user_set.clear()
	instance.team.user_set.add(*roles)


post_save.connect(mirror_members, sender=TeamRole)
post_delete.connect(mirror_members, sender=TeamRole)


