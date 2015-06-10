
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from member.functions import email_to_name
from django.utils.translation import ugettext_lazy as _


class svUser(AbstractUser):

	class Meta:
		verbose_name = _('Member')
		verbose_name_plural = _('Members')

	def get_absolute_url(self):
		return reverse('member_profile', kwargs = {'pk': self.pk, 'label': slugify(self.get_full_name())})

	def get_full_name(self):
		return super().get_full_name() or email_to_name(self.email)


