from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'display_image')
    search_fields = ('title', 'author__username', 'author__email')
    list_filter = ('author', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        ('اطلاعات پست', {'fields': ('title', 'content', 'author', 'image')}),
        ('تاریخ', {'fields': ('created_at',)}),
    )

    readonly_fields = ('created_at',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:5px;" />', obj.image.url)
        return "❌ بدون تصویر"

    display_image.short_description = "تصویر پست"
