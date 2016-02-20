from django.core.urlresolvers import reverse
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu


class MemberMenu(CMSAttachMenu):

	name = _('Member menu')

	def get_nodes(self, request):
		return [
			NavigationNode(title=_('Login'), url=reverse('account_login'), id='account_login', attr=dict(
				auth_required=False, visible_for_authenticated=False, visible_for_anonymous=True)),
			NavigationNode(title=_('Register'), url=reverse('account_signup'), id='account_signup', attr=dict(
				auth_required=False, visible_for_authenticated=False, visible_for_anonymous=True)),
			NavigationNode(title=_('Logout'), url=reverse('account_logout'), id='account_logout', attr=dict(
				auth_required=True, visible_for_authenticated=True, visible_for_anonymous=False)),

			# NavigationNode(title=_('Change password'), url=reverse('account_change_password'), id='account_change_password', attr=dict(
			# 	auth_required=False, visible_for_authenticated=False, visible_for_anonymous=True)),
			# NavigationNode(title=_('Register'), url=reverse('account_signup'), id='acc_register', attr=dict(
			# 	auth_required=False, visible_for_authenticated=False, visible_for_anonymous=True)),
			# NavigationNode(title=_('Register'), url=reverse('account_signup'), id='acc_register', attr=dict(
			# 	auth_required=False, visible_for_authenticated=False, visible_for_anonymous=True)),
			# NavigationNode(title=_('Register'), url=reverse('account_signup'), id='acc_register', attr=dict(
			# 	auth_required=False, visible_for_authenticated=False, visible_for_anonymous=True)),
			# NavigationNode(title=_('Register'), url=reverse('account_signup'), id='acc_register', attr=dict(
			# 	auth_required=False, visible_for_authenticated=False, visible_for_anonymous=True)),
			# NavigationNode(title=_('Register'), url=reverse('account_signup'), id='acc_register', attr=dict(
			# 	auth_required=False, visible_for_authenticated=False, visible_for_anonymous=True)),
			NavigationNode(title=_('Users'), url=reverse('profile_info_all'), id='profile_info_all', attr=dict(
				auth_required=True, visible_for_authenticated=True, visible_for_anonymous=False)),
			#todo: more
		]


menu_pool.register_menu(MemberMenu)


