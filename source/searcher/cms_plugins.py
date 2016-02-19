
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from searcher.models import SearchResults
from django.utils.translation import ugettext_lazy as _

#
#
# class SearchPlugin(CMSPluginBase):
# 	name = _('Search')
# 	model = SearchResults
# 	render_template = 'search_results.html'
# 	cache = False
#
# 	def render(self, context, instance, placeholder):
# 		context = super(SearchPlugin, self).render(context, instance, placeholder)
# 		context['results'] = [{}, {}]  #todo
# 		return context
#
#
# plugin_pool.register_plugin(SearchPlugin)
#
