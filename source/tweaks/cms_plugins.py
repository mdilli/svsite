
"""
Raw HTML widget.
Adapted/copied from https://github.com/makukha/cmsplugin-raw-html
"""

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template import Template
from django.utils.safestring import mark_safe
from .models import RawHtmlModel, CMSMember
from django.utils.translation import ugettext as _


class RawHtmlPlugin(CMSPluginBase):
	model = RawHtmlModel
	name = 'HTML'
	render_template = 'cms/raw_html_widget.html'
	text_enabled = True

	def render(self, context, instance, placeholder):
		context.update({
			'body': mark_safe(Template(instance.body).render(context)),
			'object': instance,
			'placeholder': placeholder
			})
		return context


plugin_pool.register_plugin(RawHtmlPlugin)


class MemberPlugin(CMSPluginBase):
	"""
	This needs to be defined in `tweaks` because it has to be after `cms`, whereas
	`AUTH_USER_MODEL` needs to be loaded before `cms`.
	"""
	model = CMSMember  # model where plugin data are saved
	module = _('Member')
	name = _('Member info')  # name of the plugin in the interface
	render_template = 'members_widget.html'

	def render(self, context, instance, placeholder):
		context.update(dict(
			inst=instance,
			title=instance.title,
			description=instance.description,
			users=instance.members.all(),
		))
		return context


plugin_pool.register_plugin(MemberPlugin)  # register the plugin


