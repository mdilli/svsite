
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from slider.models import SliderImage


class SliderImageAdmin(ModelAdmin):
	list_display = ('__str__', 'weight',)


admin.site.register(SliderImage, SliderImageAdmin)


