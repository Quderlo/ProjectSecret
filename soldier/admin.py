from django.contrib import admin

from soldier.models import Soldier


@admin.register(Soldier)
class SoldierAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'rank', 'unit')
    list_filter = ('rank', 'unit')
    search_fields = ('last_name', 'first_name', 'military_id')