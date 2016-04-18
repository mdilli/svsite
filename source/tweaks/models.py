
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



