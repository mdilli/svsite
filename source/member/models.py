
from django.contrib.auth.models import Group, UserManager, AbstractUser, GroupManager
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Member(AbstractUser):

	slug = AutoSlugField(populate_from='username', unique=True)
	birthday = models.DateField(blank=True, null=True, default=None)

	objects = UserManager()

	@property
	def teams(self):
		return Team.objects.filter(user=self)

	def __str__(self):
		return self.get_full_name()

	def get_full_name(self):
		full_name = '{0:s} {1:s}'.format(self.first_name, self.last_name)
		return full_name.strip() or self.username

	def get_short_name(self):
		return self.first_name or self.username

	def get_absolute_url(self):
		return '/'  # todo

	def has_permission_superuser(self):
		return True  # todo

	def has_permission_census(self):
		return True  # todo


class Team(Group):
	#name = models.CharField(max_length = 48, unique = True, error_messages = {'unique': 'A team with that name already exists.'})
	slug = AutoSlugField(populate_from='name', unique=True, help_text='This value is used as identifier in places like urls.')
	listed = models.BooleanField(default=False)
	description = models.TextField(default='', blank=True)
	permission_census = models.BooleanField(default=False)
	permission_superuser = models.BooleanField(default=False)
	system = models.BooleanField(default=False)
	# members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, through='teams.TeamMember')

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



# class TeamRole(models.Model):
# 	member = models.ForeignKey(settings.AUTH_USER_MODEL)
# 	team = models.ForeignKey('member.Team')
	# group = models.ForeignKey('auth.Group')
# 	admin = models.BooleanField(default=False, help_text='Admins can and and remove members and update details.')
# 	role = models.CharField(max_length=64, blank=True, default='')
#
# 	class Meta:
# 		unique_together = ('member', 'group',)
#
# 	def __str__(self):
# 		return '{0:} ∈ {1:}'.format(self.member, self.team)


