
from display_exceptions import NotFound, PermissionDenied
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms import modelformset_factory
from django.shortcuts import redirect
from base.views import render_cms_special
from svfinance.forms import PeriodForm, PeriodAccessForm
from svfinance.models import Period, PeriodAccess, Account, TransactionLine
from django.utils.translation import ugettext_lazy as _
from svfinance.utils import today


def get_period(func):
	"""
	View decorator to instantiate the period object.
	"""
	#todo: caching
	def func_with_period(request, period=None, *args, **kwargs):
		if period is None:
			period_obj = None
		else:
			try:
				period_obj = Period.objects.get(name=period)
			except Period.DoesNotExist:
				raise NotFound(_('No booking period with id "{0:s}" could be found.').format(period))
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
	for period in periods.values():
		if most_recent_period is None:
			most_recent_period = period
		elif most_recent_period.start < today_:
			if most_recent_period.start < most_recent_period.start:
				most_recent_period = period
	if most_recent_period is None:
		raise PermissionDenied('You do not have access to any bookkeeping periods. Continue to create one.', next=reverse('create_period'))
	return redirect(to=reverse('list_accounts', kwargs=dict(period=most_recent_period.slug)))


@login_required
@get_period
def edit_period(request, period=None):
	#todo: permission check
	AccessFormSet = modelformset_factory(PeriodAccess, form=PeriodAccessForm, extra=2, can_delete=True)
	if period is None:
		period_form = PeriodForm(data=request.POST or None)
		access_forms = AccessFormSet(data=request.POST or None)
	else:
		period_form = PeriodForm(data=request.POST or None, instance=period)
		access_forms = AccessFormSet(data=request.POST or None, queryset=period.accesses.all())
	period_valid = period_form.is_valid()
	access_valid = access_forms.is_valid()
	if period_valid and access_valid:
		saved_period = period_form.save()
		access_forms.save()
		return redirect(to=reverse('list_accounts', kwargs=dict(period=saved_period.slug)))
		#todo: set access instance periods?
		#todo: at least one access?
	return render_cms_special(request, 'edit_period.html', {
		'period': period,
		'period_form': period_form,
		'access_forms': access_forms,
	})


@login_required
@get_period
def list_accounts(request, period):
	#todo: permission check
	#todo: tree structure plugin (treebeard?)
	assert period is not None
	expense_acc = Account.objects.filter(period=period, type=Account.EXPENSE, parent=None)
	asset_acc = Account.objects.filter(period=period, type=Account.ASSET, parent=None)
	liability_acc = Account.objects.filter(period=period, type=Account.LIABILITY, parent=None)
	user_acc = Account.objects.filter(period=period, type=Account.DEBTCRED, parent=None)
	debtors, creditors, debtor_total, creditor_total = [], [], 0, 0
	for acc in user_acc:
		tot = acc.total()
		if tot > 0:
			debtors.append(acc)
			debtor_total += tot
		if tot < 0:
			creditors.append(acc)
			creditor_total += tot
	return render_cms_special(request, 'accounts.html', {
		'period': period,
		'expense_acc': expense_acc,
		'asset_acc': asset_acc,
		'liability_acc': liability_acc,
		'creditors': creditors,
		'creditor_total': creditor_total,
		'debtors': debtors,
		'debtor_total': debtor_total,
	})


@login_required
def list_accounts_redirect(request, period):
	return redirect(reverse('list_accounts', kwargs=dict(period=period)), permanent=True)


@login_required
@get_period
def list_account_transactions(request, period, account):
	#todo: permission check
	raise NotImplementedError('laterzz')


@login_required
@get_period
def budget_all(request, period):
	#todo: permission check
	#todo: pagination
	debtcred_other_lastaccs, debtcred_other_lines, prev_acc_chain = {}, {}, {}
	debtcred_user_lastaccs, debtcred_user_lines = {}, {user.pk: (user, []) for user in get_user_model().objects.all()}
	all_lines = {acc: [] for acc in Account.objects.filter(type=Account.DEBTCRED, period=period).order_by('pk')}
	for line in TransactionLine.objects.filter(account__type=Account.DEBTCRED).prefetch_related():
		all_lines[line.account].append(line)
	for acc, lines in all_lines.items():
		if acc.user:
			debtcred_user_lines[acc.user.pk][1].extend(lines)
			debtcred_user_lastaccs[acc.user.pk] = acc
		elif acc.prev_period_account is None:
			debtcred_other_lines[acc.pk] = list(line for line in lines)
			debtcred_other_lastaccs[acc.pk] = acc
		else:
			prev_acc_chain[acc.prev_period_account.pk] = (acc.pk, lines, acc)
	for pk, lines_li in debtcred_other_lines.items():
		child_data = prev_acc_chain.pop(pk, None)
		while child_data:
			lines_li.extend(child_data[1])
			prev_acc_chain.pop(child_data[0], None)
			debtcred_other_lastaccs[child_data[0]] = child_data[2]
	debtcred_user = tuple((debtcred_user_lastaccs[user.pk], user, sum([line.amount for line in lines], 0), lines)
		for user, lines in debtcred_user_lines.values())
	debtcred_other = tuple((acc, sum([line.amount for line in lines], 0), lines)
		for acc, lines in zip(debtcred_other_lastaccs.values(), debtcred_other_lines.values()))
	return render_cms_special(request, 'budget_all.html', {
		'period': period,
		'debtcred_user': debtcred_user,
		'debtcred_other': debtcred_other,
	})


@login_required
@get_period
def budget_user(request, user=None):
	#todo: permission check
	raise NotImplementedError('bye')


