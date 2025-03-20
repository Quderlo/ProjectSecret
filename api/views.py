from rest_framework import viewsets, permissions

from equipment.models import EquipmentModel, EquipmentType, EquipmentCategory, BattleZone
from equipment.serializers import BattleZoneModelSerializer, EquipmentCategoryModelSerializer, \
    EquipmentModelModelSerializer, EquipmentTypeModelSerializer
from soldier.models import Soldier
from soldier.serializers import SoldierModelSerializer


# Create your views here.
class SoldierViewSet(viewsets.ModelViewSet):
    queryset = Soldier.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SoldierModelSerializer

class LossRecordViewSet(viewsets.ModelViewSet):
    queryset = Soldier.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SoldierModelSerializer

class BattleZoneViewSet(viewsets.ModelViewSet):
    queryset = BattleZone.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BattleZoneModelSerializer

class EquipmentCategoryViewSet(viewsets.ModelViewSet):
    queryset = EquipmentCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipmentCategoryModelSerializer

class EquipmentModelViewSet(viewsets.ModelViewSet):
    queryset = EquipmentModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipmentModelModelSerializer

class EquipmentTypeViewSet(viewsets.ModelViewSet):
    queryset = EquipmentType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipmentTypeModelSerializer
