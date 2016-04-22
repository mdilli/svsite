
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from svfinance.models import Period, PeriodAccess
from tweaks.widgets import StartDatePicker, EndDatePicker


class PeriodForm(ModelForm):
	class Meta:
		model = Period
		fields = ('name', 'start', 'end',)
		widgets = dict(
			start = StartDatePicker(),
			end = EndDatePicker(),
		)

	def clean(self):
		super(PeriodForm, self).clean()
		if self.cleaned_data['start'] > self.cleaned_data['end']:
			self.add_error('end', 'End date cannot be before the start date.')
			#raise ValidationError('End date cannot be before the start date.')


class PeriodAccessForm(ModelForm):
	class Meta:
		model = PeriodAccess
		fields = ('team', 'can_edit',)


