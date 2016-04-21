
from django.conf.urls import url
from svfinance.views import list_transactions, auto_select_period


urlpatterns = [
	url(r'^$', auto_select_period, name='auto_select_period'),
	url(r'^(?P<period>[a-z0-9\-]+)/transactions/$', list_transactions, name='list_transactions'),
	# url(r'^$', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
	# url(r'^about/$', TemplateView.as_view(template_name = 'about.html'), name = 'about'),
	# url(r'^about/study/$', TemplateView.as_view(template_name = 'about_study.html'), name = 'about_study'),
	# url(r'^search/$', search, name = 'search'),
	# url(r'^learner/', include(learners.urls)),
	# url(r'^list/', include(lists.urls)),
	# url(r'^opinion/', include(opinions.urls)),
	# url(r'^phrase/', include(phrasebook.urls)),
	# url(r'^study/', include(study.urls)),
	# url(r'^import/', include(importing.urls)),
	# url(r'^languages/$', choose_language, name = 'choose_languages'),
	# url(r'^admin/', include(admin.site.urls)),
]


