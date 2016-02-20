
from django.conf.urls import url
from searcher.views import autocomplete, search


urlpatterns = (
	url(r'^$', search, name='search'),  #todo: tmp
	# url(r'^old/$', SearchView(template='search.html', form_class=SearchForm), name='search'),
	url(r'^complete/$', autocomplete, name='autocomplete'),
)


