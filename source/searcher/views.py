
from aldryn_search.utils import alias_from_language
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import get_language_from_request
from django.utils.html import escape
from django.views.decorators.cache import never_cache
from haystack.inputs import AutoQuery
from haystack.query import SearchQuerySet
from base.views import render_cms_special
from searcher.utils import JSONResponse


def search(request, per_page=20):
	"""
	Search pages (and more in the future) in the current language based on keywords. Filtering based on published status
	etc is already done at index level (that is, unpublished items are not included).
	"""
	query = escape(request.GET.get('q', '')).strip()

	if not query:
		paginator = Paginator([], per_page)
		page = paginator.page(1)
		count = 0
	else:
		language_code = get_language_from_request(request, check_path=True)
		connection_alias = alias_from_language(language_code)
		sqs = SearchQuerySet(using=connection_alias)
		sqs = sqs.filter(text=AutoQuery(query))

		sqs = sqs.filter(language=language_code)
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


def autocomplete(request):
	query = escape(request.GET.get('q', '')).strip()

	language_code = get_language_from_request(request, check_path=True)
	connection_alias = alias_from_language(language_code)
	sqs = SearchQuerySet(using=connection_alias)
	sqs = sqs.autocomplete(autocomplete=query)
	sqs = sqs.filter(language=language_code)
	if not request.user.is_authenticated():
		sqs = sqs.exclude(login_required=True)

	suggestions = []
	for result in sqs[:8]:
		suggestions.append({
			# 'name': Highlighter(result.text).highlight(query),
			'name': result.title,
			'url': result.url,
		})
	return JSONResponse(request, suggestions)


