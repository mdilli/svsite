
from cms.apphook_pool import apphook_pool
from django.conf.urls import url
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from member.cms_menu import MemberMenu
from member.member_urls import urlpatterns as member_urlpatterns
from member.views import member_profile_all, member_profile


class MemberApphook(CMSApp):
	name = _('Members')
	app_name = 'member'
	_urls = [member_urlpatterns]
	menus = [MemberMenu]

	def get_urls(self, page=None, language=None, **kwargs):
		"""
		This adds the public profile url for each user. The reason it doesn't just use a pattern
		is that `djangocms` cannot show/add widgets to pages by pattern, it seems.

		:param page: page the apphook is attached to
		:param language: current site language
		:return: list of urlconfs strings
		"""
		try:
			# from django.contrib.auth import get_user_model
			member_urls = [url(r'^bla/$', member_profile_all)]
			for member in get_user_model().objects.filter(is_active=True):
				member_urls.append(url(
					r'^info/{pk:d}-{label:s}/$'.format(pk=member.pk, label=member.slug),
					member_profile, kwargs=dict(pk=member.pk, label=member.slug), name='profile_info'
				))
				# member_urls.append(url(r'^{0:s}/$'.format(member.username), member_profile_all))
				# member_urls.append(member.get_absolute_url())
				# member_urls.append(reverse_lazy('profile_info', kwargs=dict(pk=member.pk, label=member.slug)))
			# print(member_urls)
			return [member_urls] + list(self._urls)
		except Exception as err:
			""" Do not silence any exception! """
			raise Exception('{0:s}'.format(str(err)))


apphook_pool.register(MemberApphook)


