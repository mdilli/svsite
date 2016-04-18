
"""
Raw HTML widget.
Adapted/copied from https://github.com/makukha/cmsplugin-raw-html
"""

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template import Template
from django.utils.safestring import mark_safe
from .models import RawHtmlModel


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


