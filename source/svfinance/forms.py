
from django.forms import ModelForm
from svfinance.models import Period, PeriodAccess


class PeriodForm(ModelForm):
	class Meta:
		model = Period
		fields = ('name', 'start', 'end',)


class PeriodAccessForm(ModelForm):
	class Meta:
		model = PeriodAccess
		fields = ('team', 'can_edit',)


