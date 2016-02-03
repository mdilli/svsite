from site import getsitepackages

from django.conf import settings
from django.contrib.auth.models import Group, UserManager, AbstractUser
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Member(AbstractUser):

	slug = AutoSlugField(populate_from='username', unique=True)
	birthday = models.DateField(blank=True, null=True, default=None)

	objects = UserManager()

	def __str__(self):
		return self.get_full_name()

	def get_full_name(self):
		full_name = '{0:s} {1:s}'.format(self.first_name, self.last_name)
		return full_name.strip() or self.username

	def get_short_name(self):
		return self.first_name or self.username

	def get_absolute_url(self):
		return '/'  # todo

getsitepackages()

# if not hasattr(Group, '_is_extended'):
# 	setattr(Group, '_is_extended', True)
# 	print(type(Member._meta.fields))
# 	for field in Member._meta.fields:
# 		if field.name != 'groups':
# 			print(type(field), field, field.name)
# 		else:
# 			print('SKIPPING', type(field), field, field.name)
	# groups = models.ManyToManyField(Group, verbose_name=_('groups'),
     # blank=True, help_text=_('The groups this user belongs to. A user will '
     #                         'get all permissions granted to each of '
     #                         'their groups.'),
     # related_name="user_set", related_query_name="user")
	#
	# AutoSlugField(populate_from='name', unique=True, help_text='This value is used as identifier in places like urls.')\
	# 	.contribute_to_class(Group, 'slug')
	# models.BooleanField(default=False)\
	# 	.contribute_to_class(Group, 'listed')
	# models.TextField(default='', blank=True)\
	# 	.contribute_to_class(Group, 'description')
	# models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, through='teams.TeamRole')\
	# 	.contribute_to_class(Member, 'teams')

#
# def mirror_teams_groups(sender, instance, action, reverse, model, pk_set, **kwargs):
# 	# http://stackoverflow.com/questions/4744794/django-cannot-detect-changes-on-many-to-many-field-with-m2m-changed-signal-au
# 	if action == 'post_add':
# 		print('add', pk_set)
# 	#todo: is this a good idea?

#
# m2m_changed.connect(mirror_teams_groups, sender=Member.groups.through)
#
#
class Team(Group):
	"""
		Proxy model extending group: http://stackoverflow.com/questions/2181039/how-do-i-extend-the-django-group-model
	"""
# 	#name = models.CharField(max_length = 48, unique = True, error_messages = {'unique': 'A team with that name already exists.'})
# 	#slug = AutoSlugField(populate_from='name', unique=True, help_text='This value is used as identifier in places like urls.')
# 	#listed = models.BooleanField(default=False)
# 	#description = models.TextField(default='', blank=True)
# 	#members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, through='teams.TeamMember')
#
# 	objects = GroupManager()
#
# 	class Meta:
# 		proxy = True
# 		verbose_name = _('Team')
# 		verbose_name_plural = _('Teams')
#
# 	def __str__(self):
# 		return self.name
#
# 	def get_absolute_url(self):
# 		# todo
# 		return reverse('group_info', kwargs = {'pk': self.pk, 'label': slugify(self.name)})
#
# 	def natural_key(self):
# 		return (self.slug,)
#
# 	def member_count(self):
# 		return self.members.count()
#
#
#
class TeamRole(models.Model):
	member = models.ForeignKey(settings.AUTH_USER_MODEL)
	team = models.ForeignKey('member.Team')
	# group = models.ForeignKey('auth.Group')
# 	admin = models.BooleanField(default=False, help_text='Admins can and and remove members and update details.')
# 	role = models.CharField(max_length=64, blank=True, default='')
#
# 	class Meta:
# 		unique_together = ('member', 'group',)
#
# 	def __str__(self):
# 		return '{0:} ∈ {1:}'.format(self.member, self.team)
#
#
