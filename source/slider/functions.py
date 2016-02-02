
from json import dumps
from time import time
from django.utils.safestring import mark_safe
from random import shuffle, randint
from slider.models import SliderImage


def slider_image_list(img_count=4, cache_timeout=60):
	"""
	Get a number of images from the collection at random, using their relative weight for the probability.
	"""
	if time() > slider_image_list._last_update + cache_timeout:
		slider_image_list._last_result = construct_slider_image_list(img_count=img_count)
		slider_image_list._last_update = time()
	return slider_image_list._last_result


slider_image_list._last_update = 0
slider_image_list._last_result = []


def construct_slider_image_list(img_count=8):
	images = list(SliderImage.objects.filter(weight__gte=1))
	if len(images) >= img_count:
		remaining = {img for img in images}
		total_weight = sum(img.weight for img in images)
		images = []
		while len(images) < img_count:
			pick = randint(0, total_weight)
			weight = 0
			for img in remaining:
				weight += img.weight
				if pick < weight:
					total_weight -= img.weight
					remaining.remove(img)
					images.append(img)
					break
	shuffle(images)
	info = []
	for img in images:
		info.append({
			'info': img.info,
			'url': img.image.url,
			'elem': None,
		})
	print(dumps(info, indent=None))
	return mark_safe(dumps(info, indent=None))


