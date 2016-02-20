
from django import template
from django.utils.timesince import timesince
from datetime import datetime
from django.utils.timezone import is_aware, utc


register = template.Library()


@register.filter()
def timesince_short(date):
	nw = datetime.now(utc if is_aware(date) else None)
	if date is None:
		return ''
	if abs(date - nw).seconds < 120:
		return 'just now'
	if date < nw:
		return '{0:s} ago'.format(*timesince(date, nw).split(','))
	else:
		return 'in {0:s}'.format(*timesince(nw, date).split(','))


