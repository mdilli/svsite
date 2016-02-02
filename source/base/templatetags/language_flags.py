
from django.template import Library
from django_countries.fields import Country


register = Library()


language_country_map = {
	'nl': 'nl',
	'en': 'gb',
	'zh': 'cn',
}


@register.simple_tag(takes_context=False)
def language_flag_url(language_code):
	language_code = language_code.lower()
	if language_code in language_country_map:
		language_code = language_country_map[language_code]
	return Country(language_code).flag


