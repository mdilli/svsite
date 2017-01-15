
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp


class SearchApphook(CMSApp):
	name = _('Search')
	app_name = 'searcher'
	# urls = ['searcher.urls']   #TODO: DEBUGGG
	menus = []


apphook_pool.register(SearchApphook)


