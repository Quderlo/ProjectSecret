from django.urls import path

from equipment import views

urlpatterns = [
    path('battle-zones-list/', views.BattleZoneListView.as_view(), name='temp-battlezone-list'),
    path('equipment-types-list/', views.EquipmentTypeListView.as_view(), name='temp-equipmenttype-list'),
]