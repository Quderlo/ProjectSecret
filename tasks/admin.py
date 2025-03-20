from django.contrib import admin
from django.utils.html import format_html

from tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'external_url', 'file_link', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    readonly_fields = ('created_at', 'file_preview')
    fieldsets = (
        (None, {
            'fields': ('title', 'external_url', 'file', 'created_at')
        }),
    )

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}">Скачать</a>', obj.file.url)
        return "-"
    file_link.short_description = 'Файл'

    def file_preview(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">{}</a>',
                             obj.file.url,
                             obj.file.name.split('/')[-1])
        return "-"
    file_preview.short_description = 'Архив'