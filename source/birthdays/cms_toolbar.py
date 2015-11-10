

from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from birthdays.models import BirthdaysPlugin
from member.models import Member


@toolbar_pool.register  # didn't register since birthdays don't need a toolbar item
class BirthdayToolbar(CMSToolbar):
	#following http://docs.django-cms.org/en/latest/introduction/toolbar.html

	supported_apps = (
		'birthdays',  # this is already set automatically to current app
	)
	watch_models = [BirthdaysPlugin, Member,]

	def populate(self):
		if not self.is_current_app:
			return

		# self.request exists

		menu = self.toolbar.get_or_create_menu('birthdays', _('Birthdays'))

		# menu.add_sideframe_item(
		# 	name=_('Poll list'),
		# 	url=admin_reverse('polls_poll_changelist'),
		# )

		menu.add_modal_item(
			name=_('Go to list'),
			url=admin_reverse('birthdays_plugin_overview'),
		)


