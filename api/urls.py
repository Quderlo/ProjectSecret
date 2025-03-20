from rest_framework import routers

from api.views import SoldierViewSet, BattleZoneViewSet, EquipmentCategoryViewSet, EquipmentModelViewSet, \
    EquipmentTypeViewSet

router = routers.DefaultRouter()

router.register('soldier', SoldierViewSet, basename='soldier')
router.register(r'battle-zones', BattleZoneViewSet, basename='battle-zones')
router.register(r'equipment-categories', EquipmentCategoryViewSet, basename='equipment-categories')
router.register(r'equipment-models', EquipmentModelViewSet, basename='equipment-models')
router.register(r'equipment-types', EquipmentTypeViewSet, basename='equipment-types')

urlpatterns = router.urls