

from django.contrib import auth
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, Permission, \
	_user_get_all_permissions, _user_has_perm, _user_has_module_perms, UserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import m2m_changed
from django.utils import timezone
from teams.models import Team, TeamMember
from django.utils.translation import ugettext_lazy as _


class Member(AbstractBaseUser):
	username = models.SlugField(unique = True, error_messages = {'unique':'A user with that username already exists.'})
	is_staff = models.BooleanField(_('staff status'), default = False, help_text = 'Designates whether the user can log into this admin site.')
	is_active = models.BooleanField(_('active'), default = True, help_text = 'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
	date_joined = models.DateTimeField(_('date joined'), default = timezone.now)

	is_superuser = models.BooleanField(_('superuser status'), default = False, help_text = _('Designates that this user has all permissions without explicitly assigning them.'))
	groups = models.ManyToManyField('teams.Team', blank = True, through = 'teams.TeamMember')
	user_permissions = models.ManyToManyField(Permission, blank = True, help_text = _('Disabled; don\'t use!'), related_name="user_set", related_query_name="user")

	first_name = models.CharField(_('first name'), max_length = 32, blank = True)
	last_name = models.CharField(_('last name'), max_length = 48, blank = True)
	email = models.EmailField(_('email address'), blank = True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip() or self.username

	def get_short_name(self):
		return self.first_name or self.username

	def get_absolute_url(self):
		return '/'

	"""
		All the permission stuff beyond here is just copied from PermissionMixin;
		no need to touch it unless Django is updated.
	"""
	@property
	def user_permissions(self):
		return []

	# def clean(self):
	# 	if self.user_permissions.count():
	# 		raise ValidationError('No user permissions allowed; use groups instead.')
	# 	return super().clean()

	def get_group_permissions(self, obj=None):
		permissions = set()
		for backend in auth.get_backends():
			if hasattr(backend, "get_group_permissions"):
				permissions.update(backend.get_group_permissions(self, obj))
		return permissions

	def get_all_permissions(self, obj=None):
		return _user_get_all_permissions(self, obj)

	def has_perm(self, perm, obj=None):
		# Active superusers have all permissions.
		if self.is_active and self.is_superuser:
			return True
		# Otherwise we need to check the backends.
		return _user_has_perm(self, perm, obj)

	def has_perms(self, perm_list, obj=None):
		for perm in perm_list:
			if not self.has_perm(perm, obj):
				return False
		return True

	def has_module_perms(self, app_label):
		# Active superusers have all permissions.
		if self.is_active and self.is_superuser:
			return True

		return _user_has_module_perms(self, app_label)


def disable_user_permissions(sender, **kwargs):
	if kwargs['instance'].user_permissions.count() > 3:
		raise ValidationError("You can't assign more than three regions")

m2m_changed.connect(disable_user_permissions, sender = Member.user_permissions)


# mg = Member.groups.through
# for f in dir(mg._meta.fields):
# 	print(f)
#
#
# if not hasattr(mg, 'admin'):
# 	admin = models.BooleanField(default = False, help_text = 'Admins can change group properties and add/remove members.')
# 	admin.contribute_to_class(mg, 'admin')


