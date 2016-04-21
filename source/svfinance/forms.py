
from django.forms import ModelForm
from svfinance.models import Period, PeriodAccess
from tweaks.widgets import DatePicker


class PeriodForm(ModelForm):
	class Meta:
		model = Period
		fields = ('name', 'start', 'end',)
		widgets = dict(
			start = DatePicker(),
			end = DatePicker(),
		)


class PeriodAccessForm(ModelForm):
	class Meta:
		model = PeriodAccess
		fields = ('team', 'can_edit',)


