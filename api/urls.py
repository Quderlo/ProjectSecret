from django.urls import path
from rest_framework import routers

from api.views import SoldierViewSet, BattleZoneViewSet, EquipmentCategoryViewSet, EquipmentModelViewSet, \
    EquipmentTypeViewSet, LossRecordsViewSet, PaymentByZoneAPI, PaymentByEquipmentAPI, \
    PaymentTimelineAPI

router = routers.DefaultRouter()

router.register('soldier', SoldierViewSet, basename='soldier')
router.register(r'battle-zones', BattleZoneViewSet, basename='battle-zones')
router.register(r'equipment-categories', EquipmentCategoryViewSet, basename='equipment-categories')
router.register(r'equipment-models', EquipmentModelViewSet, basename='equipment-models')
router.register(r'equipment-types', EquipmentTypeViewSet, basename='equipment-types')
router.register(r'loss-records', LossRecordsViewSet, basename='loss-records')


urlpatterns = router.urls

urlpatterns += [
    path('payments-by-zone/', PaymentByZoneAPI.as_view()),
    path('payments-by-equipment/', PaymentByEquipmentAPI.as_view()),
    path('payments-timeline/', PaymentTimelineAPI.as_view()),
]