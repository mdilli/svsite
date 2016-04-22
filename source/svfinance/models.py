
from adminsortable.models import SortableMixin
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
from django.db.models import CharField, Model, DecimalField, ForeignKey, PositiveSmallIntegerField, \
	DateTimeField, TextField, DateField, OneToOneField, BooleanField
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from member.models import Team, Member
from .utils import CODE_VALIDATORS, to_code, today


class Period(Model):
	name = CharField(max_length=16, validators=CODE_VALIDATORS, unique=True)
	slug = AutoSlugField(populate_from='name', editable=True)
	start = DateField()
	end = DateField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('list_accounts', kwargs=dict(period=self.slug))


class PeriodAccess(Model):
	team = ForeignKey(Team, related_name='periods_accesses')
	period = ForeignKey(Period, related_name='accesses')
	can_edit = BooleanField(default=False)

	def __str__(self):
		return '{0:} can {2:s} {1:}'.format(self.team, self.period, 'edit' if self.can_edit else 'view')


class Account(SortableMixin):

	EXPENSE, ASSET, LIABILITY, DEBTCRED, CATEGORY = 1, 2, 3, 4, 5

	name = CharField(max_length=48, help_text=_('Names should start with a letter and contain only '
		'letters, numbers and interpunction (like .,-_).'))
	code = CharField(max_length=48, validators=CODE_VALIDATORS, blank=True, default=None,
		help_text='will be automatically determined from the name if empty')

	type = PositiveSmallIntegerField(choices=(
		(EXPENSE, _('Expenses')),
		(ASSET, _('Asset')),
		(LIABILITY, _('Liability')),
		(DEBTCRED, _('Debtor/creditor')),
	))
	order = PositiveSmallIntegerField(default=0, help_text=_('This determined in which order the accounts are '
		'displayed in reports.'))

	period = ForeignKey(Period, related_name='accounts')
	prev_period_account = OneToOneField('self', blank=True, null=True, related_name=_('next_period_account'),
		help_text=_('Which account corresponds to this one in the last booking period, if any?'))
	user = ForeignKey(settings.AUTH_USER_MODEL, related_name='finance_accounts', blank=True, null=True,
		help_text='If this is a debtor/creditor account, set the user here.')  # FK because one for each period
	parent = ForeignKey('self', related_name='children', blank=True, null=True)
	is_category = BooleanField(default=False, help_text='Category accounts are just for organization. '
		'You can add other accounts as children, but cannot add. Only same-type accounts can be children.')

	class Meta:
		unique_together = (('period', 'name',), ('period', 'code'),)
		ordering = ('order',)

	def save(self, *args, **kwargs):
		if self.code is None:
			print('converting code:', self.code, '->', to_code(self.code))
			self.code = to_code(self.name)
		if self.type == self.DEBTCRED:
			""" One can have a debtor/creditor account without user linked. """
		else:
			if self.user:
				raise ValidationError(_('Only debtor/creditor accounts should have a user set.'))
		if self.parent:
			if self.period != self.parent.period:
				raise ValidationError(_('Parent must be in the same booking period.'))
			if not self.parent.is_category:
				raise ValidationError(_('Parent can only be an account marked as is_category.'))
			if self.parent.type != self.type:
				raise ValidationError(_('Children should have the same type as their parent.'))
			if self.type == self.DEBTCRED:
				raise ValidationError(_('Debtor/creditor accounts should not have parents.'))
		return super(Account, self).save(*args, **kwargs)

	def total(self):
		return sum(line.amount for line in self.lines.all())

	def stotal(self):
		return '€ {0:.2f}'.format(self.total())

	def get_absolute_url(self):
		return reverse('list_account_transactions', kwargs=dict(period=self.period.slug, account=self.code))

	def __str__(self):
		return self.name


class Transaction(Model):
	message = TextField(validators=[MinLengthValidator(4)])
	date = DateField(default=today)
	created_by = ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
	created_on = DateTimeField(default=None)
	edited_by = ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
	edited_on = DateTimeField(default=now)

	def is_valid(self):
		return self.difference() == 0.0

	def difference(self):
		return sum(line.amount for line in self.lines.all())

	def save(self, *args, **kwargs):
		#todo: all lines should belong to the same period
		if self.pk is None:
			self.created_on = now()
		self.edited_on = now()
		super(Transaction, self).save(*args, **kwargs)

	def __str__(self):
		diff = self.difference()
		if diff:
			return 'INVALID: {0:s}'.format(self.message)
		return self.message

	def get_period(self):
		try:
			return self.lines.all()[0].account.period
		except IndexError:
			return None

	def get_absolute_url(self):
		period = self.get_period()
		if period:
			return reverse('transaction', kwargs=dict(period=period.slug, transaction=self.pk))
		return reverse('transaction', kwargs=dict(transaction=self.pk))


class TransactionLine(Model):
	transaction = ForeignKey(Transaction, related_name='lines')
	amount = DecimalField(max_digits=12, decimal_places=2)
	account = ForeignKey(Account, blank=True, null=True, related_name='lines')

	# def save(self, *args, **kwargs):
		# if (self.balance_account is None) == (self.expense_account is None):
		# 	raise ValidationError('Either balance_account or expense_account should be set, but not both.')
		# super(TransactionLine, self).save(*args, **kwargs)

	def __str__(self):
		return '#{0:d} ({1:})'.format(self.pk, self.transaction)

	def get_absolute_url(self):
		return '{0:s}#line-{1:d}'.format(self.transaction.get_absolute_url(), self.pk)


class TransactionValidation(Model):
	auditor = ForeignKey(Team, related_name='+')
	transaction = ForeignKey(Transaction, related_name='validations')
	when = DateTimeField(auto_now_add=True)

	@property
	def is_valid(self):
		return self.when < self.transaction.edited_on

	def __str__(self):
		return '{0:s} validated {1:}'.format(self.auditor, self.transaction)


def user_to_debtor_creditor_on_user(signal, using, sender, instance, **kwargs):
	unfinished_periods = Period.objects.filter(end__gt=today())
	for period in unfinished_periods:
		user_accs = Account.objects.filter(user=instance, period=period)
		if not user_accs:
			# does not set `prev_period_account`
			account = Account(period=period, user=instance, name=instance.username, type=Account.DEBTCRED)
			account.save()


def user_to_debtor_creditor_on_period(signal, using, sender, instance, **kwargs):
	for user in Member.objects.filter(is_active=True):
		user_accs = Account.objects.filter(user=user, period=instance)
		if not user_accs:
			# does not set `prev_period_account`
			account = Account(user=user, period=instance, name=user.username, type=Account.DEBTCRED)
			account.save()
	#todo: extrapolate previous when a period is made


post_save.connect(user_to_debtor_creditor_on_user, sender=Member)
post_save.connect(user_to_debtor_creditor_on_period, sender=Period)


