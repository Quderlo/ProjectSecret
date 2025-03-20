from django.contrib import admin

from statistic.models import LossRecords


# Register your models here.
@admin.register(LossRecords)
class LossRecordsAdmin(admin.ModelAdmin):
    list_display = ('soldier', 'equipment_type', 'battle_zone', 'date', 'quantity')
    list_filter = ('date', 'battle_zone', 'equipment_type')
    search_fields = ('soldier__last_name', 'equipment_type__name')
    date_hierarchy = 'date'