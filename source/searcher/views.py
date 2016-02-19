
from cms.plugin_rendering import render_placeholder
from django.shortcuts import render
from django.template import RequestContext
from django.template.defaultfilters import striptags
from django.utils.html import escape
from django.views.decorators.cache import never_cache
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter
from searcher.models import SearchResults
from searcher.utils import JSONResponse


def search(request):
	# render_placeholder(SearchResults.objects.all()[0])
	return render(request, 'search.html', dict(
		search_result=SearchResults.objects.all()[0],
	))


@never_cache  # todo: remove
def autocomplete(request):
	query = escape(request.GET.get('q', '')).strip()
	if len(query) < 2:
		suggestions = []
	else:
		lighter = Highlighter(query, max_length=32)
		sqs = SearchQuerySet().autocomplete(auto=query)[:7]
		suggestions = []
		for result in sqs:
			match = ' '.join(striptags(lighter.highlight(result.auto)).strip('.').split())
			url = None
			if hasattr(result.object, 'get_absolute_url'):
				url = result.object.get_absolute_url()
			suggestions.append({
				'name': match,
				'url': url,
			})
	return JSONResponse(request, suggestions)


