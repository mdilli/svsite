
from django.template import Library, Context
from django.template.loader import render_to_string
from slider.functions import slider_image_list


register = Library()


@register.simple_tag(takes_context=False)
def load_attach_image_slider(header_selector):
	return render_to_string('image_slider.html', Context({
		'image_list': slider_image_list(),
		'header_selector': header_selector,
	}))


