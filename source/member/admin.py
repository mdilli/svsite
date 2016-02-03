
from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from member.models import Member


class MemberAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	#todo: add teams back in some way?


site.register(Member, MemberAdmin)


