
from haystack.forms import HighlightedSearchForm


class SearchForm(HighlightedSearchForm):

	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['q'].widget.attrs['placeholder'] = 'Your search query...'
		self.fields['q'].widget.attrs['autofocus'] = 'autofocus'
		self.fields['q'].widget.attrs['autocomplete'] = 'off'
		self.fields['q'].widget.attrs['class'] = self.fields['q'].widget.attrs.get('class', '') + ' search-typeahead'


