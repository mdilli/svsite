
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from member.functions import email_to_name


class svUser(AbstractUser):


	def get_absolute_url(self):
		return reverse('member_profile', kwargs = {'pk': self.pk, 'label': slugify(self.get_full_name())})

	def get_full_name(self):
		return super().get_full_name() or email_to_name(self.email)


