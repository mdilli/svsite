
from aldryn_search.utils import alias_from_language
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import get_language_from_request
from django.template.defaultfilters import striptags
from django.utils.html import escape
from django.views.decorators.cache import never_cache
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from haystack.utils import Highlighter
from base.views import render_cms_special
from searcher.utils import JSONResponse


def search(request, per_page=20):

	#todo: I get results in wrong languages and ones that don't match

	query = escape(request.GET.get('q', '')).strip()

	if not query:
		paginator = Paginator([], per_page)
		page = paginator.page(1)
		count = 0
	else:
		language = get_language_from_request(request, check_path=True)
		connection_alias = alias_from_language(language)
		sqs = SearchQuerySet(using=connection_alias)
		sqs.auto_query(query) #todo

		if not request.user.is_authenticated():
			sqs = sqs.exclude(login_required=True)
		count = sqs.count()

		paginator = Paginator(sqs, per_page)
		try:
			page = paginator.page(request.GET.get('page', 1))
		except PageNotAnInteger:
			page = paginator.page(1)
		except EmptyPage:
			page = Paginator(sqs, per_page)

	return render_cms_special(request, 'search_content.html', dict(
		query=query,
		count=count,
		results=page,
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


