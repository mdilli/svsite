
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from birthdays.menu import BirthdaysMenu


class BirthdaysApp(CMSApp):
	# following http://docs.django-cms.org/en/latest/introduction/apphooks.html
	name = _('Full birthdays list')
	# urls = ['birthdays.urls']   #TODO: DEBUGGG
	app_name = 'birthdays'
	menus = [BirthdaysMenu]


apphook_pool.register(BirthdaysApp)


