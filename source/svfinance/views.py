
from display_exceptions import NotFound, PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms import formset_factory
from django.shortcuts import redirect
from base.views import render_cms_special
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
		if period is None:
			period_obj = None
		else:
			try:
				period_obj = Period.objects.get(name=period)
			except Period.DoesNotExist:
				raise NotFound(_('No booking period with id "{0:s}" could be found.').format())
		return func(request, period_obj, *args, **kwargs)
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
		raise PermissionDenied('You do not have access to any bookkeeping periods. Continue to create one.', next=reverse('create_period'))
	return redirect(to=reverse('list_transactions', kwargs=dict(slug=most_recent_period.slug)))


# @login_required
# def create_period(request):
# 	period_form = PeriodForm()
# 	AccessFormSet = formset_factory(PeriodAccessForm, extra=2, can_delete=True)
# 	access_forms = AccessFormSet()
# 	return render_cms_special(request, 'edit_period.html', {
# 		'period': None,
# 		'period_form': period_form,
# 		'access_forms': access_forms,
# 	})


@login_required
@get_period
def edit_period(request, period):
	print(period)
	AccessFormSet = formset_factory(PeriodAccessForm, extra=2, can_delete=True)
	if period is None:
		period_form = PeriodForm()
		access_forms = AccessFormSet()
	else:
		period_form = PeriodForm(instance=period)
		access_forms = AccessFormSet(queryset=period.accesses.all())
	return render_cms_special(request, 'edit_period.html', {
		'period': period,
		'period_form': period_form,
		'access_forms': access_forms,
	})


