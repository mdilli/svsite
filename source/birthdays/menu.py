
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from member.models import Member


class BirthdaysMenu(CMSAttachMenu):
	# following http://docs.django-cms.org/en/latest/introduction/menu.html

	name = _('Birthdays menu')  # give the menu a name this is required.

	def get_nodes(self, request):
		"""
		This method is used to build the menu tree.
		"""
		nodes = [] #todo
		# note how this menu is not for a specific plugin but rather is more general (we have no plugin instance)
		for birthday_user in Member.objects.all():
			node = NavigationNode(
				title=birthday_user.get_full_name(),
				url=birthday_user.get_absolute_url(),
				id=birthday_user.pk,  # well that's what the demo did...
			)
			nodes.append(node)
		nodes.append(NavigationNode(
			title='</birthdays>',
			url='/',
			id=9999,
		))
		return nodes


menu_pool.register_menu(BirthdaysMenu)


