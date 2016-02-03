from django.contrib.admin import ModelAdmin

from activity.models import Activity
from base.admin import superuser_admin


class ActivityAdmin(ModelAdmin):
	list_display = ('name', 'start', 'member_cost', 'outsider_allowed', 'registration_mode', 'registration_deadline',)
	list_filter = ('start', 'member_cost', 'outsider_allowed', 'registration_mode', 'registration_deadline',)
	#todo: conditional-show registration_deadline and outsider_cost
	#todo: set end time automatically after start time is set


superuser_admin.register(Activity, ActivityAdmin)


