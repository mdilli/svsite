
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeFramedModel


class Activity(TimeFramedModel):

	name = models.CharField(max_length = 64)
	description = models.TextField(blank = True)
	#start = models.DateTimeField(blank = True, null = True, help_text = 'When does the event start?')
	#end = models.DateTimeField(blank = True, null = True, help_text = 'When does the event end?')
	member_cost = models.DecimalField(max_digits = 8, decimal_places = 2, help_text = 'Cost for attending this event')
	outsider_allowed = models.BooleanField(default = True, help_text = 'Are non-members welcome at this event?')
	outsider_cost = models.DecimalField(max_digits = 8, decimal_places = 2, help_text = 'Cost for attending this event if you are not a member')
	registration_mode = models.CharField(choices = (
		('no', 'No registration'),
		('possible', 'Registration possible'),
		('suggested', 'Registration suggested'),
		('required', 'Registration required'),
	), max_length = 12, help_text = 'Do visitors register?')
	registration_deadline = models.DateTimeField(blank = True, null = True, help_text = 'After which time does registration close?')
	#todo: location field
	#todo: image field
	#todo: db constraint end time after start

	class Meta:
		verbose_name = _('activity')
		verbose_name_plural = _('activities')

	def get_absolute_url(self):
		return reverse('activity_info', kwargs = {'pk': self.pk, 'label': slugify(self.name)})


