
from adminsortable.models import SortableMixin
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db.models import CharField, Model, DecimalField, ForeignKey, PositiveSmallIntegerField, \
	DateTimeField, TextField, DateField, OneToOneField, BooleanField
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from member.models import Team
from .utils import CODE_VALIDATORS, to_code, today


class Period(Model):
	name = CharField(max_length=16, validators=CODE_VALIDATORS)
	slug = AutoSlugField(populate_from='name', editable=True)
	start = DateField()
	end = DateField()


class PeriodAccess(Model):
	team = ForeignKey(Team, related_name='periods_accesses')
	period = ForeignKey(Period, related_name='accesses')
	can_edit = BooleanField(default=False)


class Account(SortableMixin):

	EXPENSE, ASSET, LIABILITY, USER, CATEGORY = 1, 2, 3, 4, 5

	name = CharField(max_length=48, unique=True, help_text=_('Names should start with a letter and contain only '
		'letters, numbers and interpunction (like .,-_).'))
	code = CharField(max_length=48, unique=True, validators=CODE_VALIDATORS, blank=True, default=None)

	type = PositiveSmallIntegerField(choices=(
		(EXPENSE, _('Expenses')),
		(ASSET, _('Expenses')),
		(LIABILITY, _('Expenses')),
		(USER, _('Debtor/creditor')),
		(CATEGORY, _('Category')),
	))
	order = PositiveSmallIntegerField(help_text=_('This determined in which order the accounts are '
		'displayed in reports.'))

	period = ForeignKey(Period, related_name='accounts')
	prev_period_account = OneToOneField('self', blank=True, null=True, related_name=_('next_period_account'),
		 help_text=_('Which account corresponds to this one in the last booking period, if any?'))
	user = ForeignKey(settings.AUTH_USER_MODEL, related_name='finance_accounts', blank=False, null=True)
	parent = ForeignKey('self', related_name='children', blank=True, null=True)

	class Meta:
		ordering = ('order',)

	def save(self, *args, **kwargs):
		if self.code is None:
			self.code = to_code(self.name)
		if self.user is not None and self.type is not self.USER:
			raise ValidationError(_('User should not be set unless this is a user account.'))
		super(Account, self).save(*args, **kwargs)


class Transaction(Model):
	message = TextField(validators=[MinLengthValidator(4)])
	date = DateField(default=today)
	created_by = ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
	created_on = DateTimeField(default=None)
	edited_by = ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
	edited_on = DateTimeField(default=now)

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.created_on = now()
		self.edited_on = now()
		super(Transaction, self).save(*args, **kwargs)


class TransactionLine(SortableMixin):
	transaction = ForeignKey(Transaction, related_name='lines')
	amount = DecimalField(max_digits=12, decimal_places=2)
	account = ForeignKey(Account, blank=True, null=True, related_name='transaction_lines')

	# def save(self, *args, **kwargs):
	# 	if (self.balance_account is None) == (self.expense_account is None):
	# 		raise ValidationError('Either balance_account or expense_account should be set, but not both.')
	# 	super(TransactionLine, self).save(*args, **kwargs)


class TransactionValidation(Model):
	auditor = ForeignKey(Team, related_name='+')
	transaction = ForeignKey(Transaction, related_name='validations')
	when = DateTimeField(auto_now_add=True)

	@property
	def is_valid(self):
		return self.when < self.transaction.edited_on


