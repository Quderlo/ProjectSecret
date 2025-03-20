from django.contrib import admin
from .models import BattleZone, EquipmentCategory, EquipmentModel, EquipmentType

@admin.register(BattleZone)
class BattleZoneAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 20

@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name")
    search_fields = ("display_name",)
    ordering = ("display_name",)

@admin.register(EquipmentModel)
class EquipmentModelAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "category")
    search_fields = ("display_name",)
    list_filter = ("category",)
    ordering = ("display_name",)

@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "model", "get_category")
    search_fields = ("name",)
    list_filter = ("model__category", "model")
    ordering = ("name",)

    def get_category(self, obj):
        return obj.model.category.display_name
    get_category.short_description = "Категория техники"
