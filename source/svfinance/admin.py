
# todo: this is temporary

from django.contrib.admin import ModelAdmin, TabularInline
from base.admin import superuser_admin
from svfinance.models import Period, PeriodAccess, Account, Transaction, TransactionLine, TransactionValidation


class PeriodAccessInlineAdmin(TabularInline):
	model = PeriodAccess


class PeriodAdmin(ModelAdmin):
	model = Period
	list_display = ('name', 'start', 'end',)
	inlines = (PeriodAccessInlineAdmin,)


class AccountAdmin(ModelAdmin):
	list_display = ('name', 'period', 'type', 'is_category', 'parent', 'stotal',)
	model = Account


class TransactionLineInlineAdmin(TabularInline):
	model = TransactionLine


class TransactionValidationInlineAdmin(TabularInline):
	model = TransactionValidation


class TransactionAdmin(ModelAdmin):
	model = Transaction
	inlines = (TransactionLineInlineAdmin, TransactionValidationInlineAdmin,)


superuser_admin.register(Period, PeriodAdmin)
superuser_admin.register(Account, AccountAdmin)
superuser_admin.register(Transaction, TransactionAdmin)


