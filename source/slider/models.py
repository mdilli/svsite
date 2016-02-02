
import django_resized
from django.conf import settings
from django.db import models


class SliderImage(models.Model):
	weight = models.PositiveSmallIntegerField(default=1, help_text='How likely is this image to show up?')
	image = django_resized.ResizedImageField(size=(settings.SLIDER_IMG_WIDTH, settings.SLIDER_IMG_HEIGHT),
		crop=['middle', 'center'],	quality=85, keep_meta=False, upload_to='slider',
		help_text=('Images should be at least {0:d}x{1:d}, or they will be scaled up, reducing quality.')
			.format(settings.SLIDER_IMG_WIDTH, settings.SLIDER_IMG_HEIGHT),
	)
	info = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.info or 'image #{0:}'.format(self.pk)


