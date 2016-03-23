
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from member.cms_menu import MemberMenu


class MemberApphook(CMSApp):
	name = _('Members')
	app_name = 'member'
	urls = ['member.member_urls']
	menus = [MemberMenu]


apphook_pool.register(MemberApphook)


