
from aldryn_search.base import AldrynIndexBase
from haystack import indexes


class TitleACIndex(AldrynIndexBase):
	"""
	Like Aldryn index, but with autocomplete.
	"""
	index_title = True

	autocomplete = indexes.NgramField()

	def prepare_autocomplete(self, object):
		return '{0:}\n{1:}\n{2:}'.format(object.title, object.page_title, object.menu_title)


