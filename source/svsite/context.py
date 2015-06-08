
from django.contrib.sites.shortcuts import get_current_site
from svsite import settings


"""
	put some settings into the default context
	note that misc has a similar processor; your setting may already be added
"""
def context_settings(request):
	site = get_current_site(request)
	return {
		'BASE_TEMPLATE': settings.BASE_TEMPLATE,
		'BASE_EMAIL_TEMPLATE': settings.BASE_EMAIL_TEMPLATE,
		'SITE_NAME': site.name,
		'SITE_DOMAIN': site.domain,
	}


