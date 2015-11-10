
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from birthdays.models import BirthdaysPluginModel


class CMSBirthdaysPlugin(CMSPluginBase):  # subclass of ModelAdmin
	# following http://docs.django-cms.org/en/latest/introduction/plugins.html
	# and see http://docs.django-cms.org/en/latest/how_to/custom_plugins.html

	model = BirthdaysPluginModel
	module = _('Member')
	name = _('Upcomming birthdays')
	render_template = 'birthdays_plugin.html'
	cache = True

	def render(self, context, instance, placeholder):

		birthday_users = instance.birthdays()
		context.update({
			'instance': instance,
			'birthday_users': birthday_users,
		})
		return context


plugin_pool.register_plugin(CMSBirthdaysPlugin)


