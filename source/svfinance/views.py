
from display_exceptions import NotFound, PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from svfinance.forms import PeriodForm, PeriodAccessForm
from svfinance.models import Period
from django.utils.translation import ugettext_lazy as _
from svfinance.utils import today


def get_period(func):
	"""
	View decorator to instantiate the period object.
	"""
	#todo: caching
	def func_with_period(request, period, *args, **kwargs):
		try:
			period_obj = Period.objects.get(name=period)
		except Period.DoesNotExist:
			raise NotFound(_('No booking period with id "{0:s}" could be found.').format())
		func(request, period_obj, *args, **kwargs)
	return func_with_period


@login_required
def auto_select_period(request):
	"""
	From among periods you have access to, find the most-recently started.
	"""
	periods = dict()
	for team in request.user.teams:
		for access in team.periods_accesses.prefetch_related():
			periods[access.period.pk] = access.period
	most_recent_period = None
	today_ = today()
	for period in periods:
		if most_recent_period is None:
			most_recent_period = period
		elif most_recent_period.start < today_:
			if most_recent_period.start < most_recent_period.start:
				most_recent_period = period
	if most_recent_period is None:
		raise PermissionDenied('You do not have access to any bookkeeping periods.')
	return redirect(to=reverse('list_transactions', kwargs=dict(slug=most_recent_period.slug)))


@login_required
@get_period
def list_transactions(request, period):
	print(period)
	period_form = PeriodForm(instance=period)
	access_forms = PeriodAccessForm(queryset=period.accesses)
	pass

