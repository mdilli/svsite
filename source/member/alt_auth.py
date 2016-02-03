
from __future__ import unicode_literals
from django.contrib import auth
from django.contrib.auth.models import Permission, _user_get_all_permissions, _user_has_perm, _user_has_module_perms, \
	AbstractBaseUser, UserManager, AbstractUser
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


"""
This is intentionally almost literally copied from auth. A lot of copy-pasting which isn't great,
but it's less ugly and more reliable than dynamically patching the model. The difference so far
is just the groups having a link to Team (which extends group), connected through TeamRole.
"""


class AltPermissionsMixin(models.Model):
	"""
	A mixin class that adds the fields and methods necessary to support
	Django's Group and Permission model using the ModelBackend.
	"""
	is_superuser = models.BooleanField(_('superuser status'), default=False,
		help_text=_('Designates that this user has all permissions without '
					'explicitly assigning them.'))
	groups = models.ManyToManyField('member.Team', verbose_name=_('groups'), through='member.TeamRole',
		blank=True, help_text=_('The groups this user belongs to. A user will '
								'get all permissions granted to each of '
								'their groups.'),
		related_name="user_set", related_query_name="user")
	user_permissions = models.ManyToManyField(Permission,  # todo: remove maybe? or just hide
		verbose_name=_('user permissions'), blank=True,
		help_text=_('Specific permissions for this user.'),
		related_name="user_set", related_query_name="user")

	class Meta:
		abstract = True

	def get_group_permissions(self, obj=None):
		"""
		Returns a list of permission strings that this user has through their
		groups. This method queries all available auth backends. If an object
		is passed in, only permissions matching this object are returned.
		"""
		permissions = set()
		for backend in auth.get_backends():
			if hasattr(backend, "get_group_permissions"):
				permissions.update(backend.get_group_permissions(self, obj))
		return permissions

	def get_all_permissions(self, obj=None):
		return _user_get_all_permissions(self, obj)

	def has_perm(self, perm, obj=None):
		"""
		Returns True if the user has the specified permission. This method
		queries all available auth backends, but returns immediately if any
		backend returns True. Thus, a user who has permission from a single
		auth backend is assumed to have permission in general. If an object is
		provided, permissions for this specific object are checked.
		"""

		# Active superusers have all permissions.
		if self.is_active and self.is_superuser:
			return True

		# Otherwise we need to check the backends.
		return _user_has_perm(self, perm, obj)

	def has_perms(self, perm_list, obj=None):
		"""
		Returns True if the user has each of the specified permissions. If
		object is passed, it checks if the user has all required perms for this
		object.
		"""
		for perm in perm_list:
			if not self.has_perm(perm, obj):
				return False
		return True

	def has_module_perms(self, app_label):
		"""
		Returns True if the user has any permissions in the given app label.
		Uses pretty much the same logic as has_perm, above.
		"""
		# Active superusers have all permissions.
		if self.is_active and self.is_superuser:
			return True

		return _user_has_module_perms(self, app_label)


class AltAbstractUser(AbstractBaseUser, AltPermissionsMixin):
	"""
	An abstract base class implementing a fully featured User model with
	admin-compliant permissions.

	Username, password and email are required. Other fields are optional.
	"""
	username = models.CharField(_('username'), max_length=30, unique=True,
		help_text=_('Required. 30 characters or fewer. Letters, digits and '
					'@/./+/-/_ only.'),
		validators=[
			validators.RegexValidator(r'^[\w.@+-]+$',
									  _('Enter a valid username. '
										'This value may contain only letters, numbers '
										'and @/./+/-/_ characters.'), 'invalid'),
		],
		error_messages={
			'unique': _("A user with that username already exists."),
		})
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	email = models.EmailField(_('email address'), blank=True)
	is_staff = models.BooleanField(_('staff status'), default=False,
		help_text=_('Designates whether the user can log into this admin '
					'site.'))
	is_active = models.BooleanField(_('active'), default=True,
		help_text=_('Designates whether this user should be treated as '
					'active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')
		abstract = True

	def email_user(self, subject, message, from_email=None, **kwargs):
		"""
		Sends an email to this User.
		"""
		send_mail(subject, message, from_email, [self.email], **kwargs)


