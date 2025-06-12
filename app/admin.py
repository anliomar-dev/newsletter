from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class UserAdmin(UserAdmin):
    ordering = ['email']
    list_display = ('email',)
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribe_at')
    readonly_fields = ('subscribe_at', 'email')


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(User, UserAdmin)