
from django.template import Library


class WrongFormatException(Exception):
	""" Special exception because ValueError tends to get swallowed """


register = Library()


@register.filter
def euro(value):
	if not value:
		value = 0.
	try:
		value = float(value)
	except ValueError:
		raise WrongFormatException('|euro got "{0:}" which is not a number'.format(value))
	return '€ {0:.2f}'.format(value)


