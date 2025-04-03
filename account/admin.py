from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class UserAdmin(BaseUserAdmin):
    filter_horizontal = ()
    list_display = ('id', 'username', 'email', 'phone_number', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('-date_joined',)
    fieldsets = (
        ('اطلاعات کاربر', {'fields': ('username', 'email', 'phone_number', 'password')}),
        ('مجوزها', {'fields': ('is_active', 'is_staff')}),
        ('تاریخ‌ها', {'fields': ('date_joined',)}),
    )
    readonly_fields = ('date_joined',)

    add_fieldsets = (
        ('ایجاد کاربر جدید', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )


class PasswordResetRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'reset_code', 'created_at', 'expires_at', 'is_expired_status')
    list_filter = ('expires_at',)
    search_fields = ('user__username', 'user__email', 'user__phone_number', 'reset_code')
    ordering = ('-created_at',)

    def is_expired_status(self, obj):
        return "✅ فعال" if not obj.is_expired() else "❌ منقضی شده"

    is_expired_status.short_description = "وضعیت کد تأیید"



admin.site.register(User, UserAdmin)
admin.site.register(PasswordResetRequest, PasswordResetRequestAdmin)
