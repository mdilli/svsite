
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import svUser


admin.site.register(svUser, UserAdmin)


