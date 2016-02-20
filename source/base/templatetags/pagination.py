
from urllib.parse import urlencode
from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def pagination_url(context, page=None):
	assert 'request' in context, 'pagination_url needs RequestContext'
	params = {key: val for key, val in context['request'].GET.items() if key != 'page'}
	if page and page != 1:
		params['page'] =str(page)
	if params:
		return '{0:s}?{1:s}'.format(context['request'].path, urlencode(params))
	return context['request'].path


@register.filter()
def nearby_pages(items):
	"""
		Get a list of pages to display for pagination, and None values for continuation dots.

		Shows up to 12 values, always shows the fist and last two elements and the two elements left and right of the current one.

		See e.g. the template pagination_bootstrap.html
	"""
	if items.paginator.num_pages <= 10:
		return range(1, items.paginator.num_pages + 1)
	if items.number <= 6:
		return range(1, 9) + [None, items.paginator.num_pages, items.paginator.num_pages + 1]
	if items.number >= items.paginator.num_pages - 6:
		return [1, 2, None] + range(items.paginator.num_pages - 8, items.paginator.num_pages + 1)
	return [1, 2, None] + range(items.number - 2, items.number + 3) + [None, items.paginator.num_pages, items.paginator.num_pages + 1]


