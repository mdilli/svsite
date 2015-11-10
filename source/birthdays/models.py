
from cms.models import CMSPlugin
from datetime import timedelta
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from member.models import Member


class BirthdaysPluginModel(CMSPlugin):
	# following http://docs.django-cms.org/en/latest/introduction/plugins.html
	caption = models.CharField(max_length=32, default=_('Happy birthday to...'))
	max_days = models.PositiveSmallIntegerField(default=7, blank=True, null=True, validators=[MaxValueValidator(365)])
	max_entries = models.PositiveSmallIntegerField(default=None, blank=True, null=True)

	def birthdays(self):
		return Member.objects.filter( #todo how to query this for every year?
			birthday__gt=now(),
			birthday__lt=now()+timedelta(self.max_days)
		).order_by('birthday', 'first_name')[:self.max_entries]


