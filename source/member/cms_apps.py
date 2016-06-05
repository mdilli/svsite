
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from member.cms_menu import MemberMenu
from member.member_urls import urlpatterns as member_urlpatterns


class MemberApphook(CMSApp):
	name = _('Members')
	app_name = 'member'
	urls = [member_urlpatterns]
	menus = [MemberMenu]

	def get_urls(self, *args, **kwargs):
		print(args)
		print(kwargs)
		return [member_urlpatterns]


apphook_pool.register(MemberApphook)


