
"""
Raw HTML widget.
Adapted/copied from https://github.com/makukha/cmsplugin-raw-html
"""

from cms.models import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class RawHtmlModel(CMSPlugin):
	body = models.TextField('HTML')

	# def __str__(self):
	#     return self.body


class CMSMember(CMSPlugin):
	title = models.CharField(max_length=64, default='Members')
	description = models.TextField(blank=True)
	members = models.ManyToManyField('member.Member')

	def __unicode__(self):
		return 'CMS Member <{0:s}>'.format(', '.join(str(mem) for mem in self.members.all()))

	def copy_relations(self, old_instance):
		self.members = old_instance.members.all()


