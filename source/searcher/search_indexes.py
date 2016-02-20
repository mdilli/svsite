
from cms.models import Page, Title
from haystack.fields import CharField, EdgeNgramField
from haystack.indexes import SearchIndex, Indexable


#todo: maybe just use page-index and try to render all plugins?
#todo: can't I somehow use the actually-rendered page for search index?
#is this what aldryn-search does?
#todo: published ones only


# class CMSPageIndex(SearchIndex, Indexable):
# 	text = CharField(document=True)
# 	autocomplete = EdgeNgramField()
# 	title = CharField()
# 	url = CharField()
# 	language = CharField(model_attr='languages')
#
# 	def get_model(self):
# 		return Title
#
# 	def prepare(self, object):
# 		prepared_data = super(CMSPageIndex, self).prepare(object)
# 		#todo: for each language?
# 		langs = self.prepared_data['language'].split(',')
# 		langs = object.languages.split(',')
# 		print(langs)
# 		print(object.path)
# 		return prepared_data
#
# 	def prepare_url(self, object):
# 		return '/'



# class TitleIndex(indexes.SearchIndex, indexes.Indexable):
# 	text = indexes.CharField(document=True, use_template=True, template_name='title.index')
# 	autocomplete = indexes.EdgeNgramField(model_attr='title')
# 	title = indexes.CharField(model_attr='title')
# 	language = indexes.CharField(model_attr='language')
#
# 	def get_model(self):
# 		return Title
#
#
# class TextIndex(indexes.SearchIndex, indexes.Indexable):
# 	text = indexes.CharField(document=True, use_template=True, template_name='text.index')
# 	autocomplete = indexes.EdgeNgramField(model_attr='body')
# 	title = indexes.CharField(model_attr='body')  #todo: query for page title or something?
# 	language = indexes.CharField(model_attr='language')
#
# 	def get_model(self):
# 		return Text
#
#
