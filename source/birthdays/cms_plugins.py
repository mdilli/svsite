
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from birthdays.models import BirthdaysPlugin


class CMSBirthdaysPlugin(CMSPluginBase):
	# following http://docs.django-cms.org/en/latest/introduction/plugins.html
	model = BirthdaysPlugin
	module = _('Member')
	name = _('Upcomming birthdays')
	render_template = 'birthdays_plugin.html'

	def render(self, context, instance, placeholder):

		birthday_users = instance.birthdays()
		context.update({
			'instance': instance,
			'birthday_users': birthday_users,
		})
		return context


plugin_pool.register_plugin(CMSBirthdaysPlugin)


