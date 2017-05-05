from django.contrib import admin

# Register your models here.
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position')

admin.site.register(UserProfile,UserProfileAdmin)