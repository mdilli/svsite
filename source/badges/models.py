
from django.conf import settings
from django.db import models
from re import match


class BadgeType:
	"""
	A type of badge that one can get.
	Not a model! They should be a fixed set, not editable.
	"""
	def __init__(self, key, name, description, score, image, hash):
		assert match(r'[a-zA-Z][a-zA-Z0-9\-]{0,7}', key), 'badge keys must be unique strings of up to 8 alphanumeric characters or dashes'
		self.key = str(key)
		self.name = name
		self.description = description or ''
		self.score = score
		self.image = image
		self.hash = hash

	def __str__(self):
		return str(self.name)

	def image_url(self):
		return 'badges/{0:s}'.format(self.image)

	def awards(self):
		return BadgeAward.objects.filter(badge=self.key)


class BadgeAward(models.Model):
	"""
	An award given to a specific person.
	"""
	from badges.badges import BADGE_CHOICES
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='badges_awarded')
	badge = models.CharField(choices=BADGE_CHOICES, max_length=8)
	when = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'badge',)
		ordering = ('-pk',)


