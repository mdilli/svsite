
from django.conf.urls import url
from django.http import HttpResponse
from svfinance.views import edit_period, auto_select_period, list_accounts, \
	list_account_transactions, budget_all, budget_user, list_accounts_redirect


urlpatterns = [
	url(r'^$', auto_select_period, name='auto_select_period'),
	url(r'^new/$', edit_period, name='create_period'),
	url(r'^(?P<period>[a-z0-9\-]+)/edit/$', edit_period, name='edit_period'),
	url(r'^(?P<period>[a-z0-9\-]+)/$', list_accounts_redirect),
	url(r'^(?P<period>[a-z0-9\-]+)/accounts/$', list_accounts, name='list_accounts'),
	# url(r'^p(?P<period>[a-z0-9\-]+)/transactions/$', list_period_transactions, name='list_period_transactions'),
	url(r'^(?P<period>[a-z0-9\-]+)/(?P<account>[a-z0-9\-]+)/transactions/$', list_account_transactions, name='list_account_transactions'),
	url(r'^budgets/$', budget_all, name='budget_all'),
	url(r'^(?P<period>[a-z0-9\-]+)/budgets/$', budget_all, name='budget_all'),
	# url(r'^(?P<period>[a-z0-9\-]+)/find_budget/$', budget_user, name='budget_user'),
	url(r'^(?P<period>[a-z0-9\-]+)/(?P<user>[a-z0-9\-]+)/budget/$', budget_user, name='budget_user'),
	url(r'^(?P<period>[a-z0-9\-]+)/~/budget/$', budget_user, name='budget_user'),
	# url(r'^(?P<user>[a-z0-9\-]+)/budget/$', budget_user, name='budget_user'),
	# url(r'^~/budget/$', budget_user, name='budget_user'),
	url(r'^~(?P<transaction>\d+)/$', lambda request: HttpResponse('Not implemented'), name='transaction'),
	url(r'^(?P<period>[a-z0-9\-]+)/transaction~(?P<transaction>\d+)/$', lambda request: HttpResponse('Not implemented'), name='transaction'),
	# todo: this is just an account overview
]


