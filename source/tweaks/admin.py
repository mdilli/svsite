
from cms.models import PageUser
from django.contrib import admin

# Register your models here.

def shrink_cms_admin():
	admin.site.unregister(PageUser)


