from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from equipment.models import EquipmentModel, EquipmentType, EquipmentCategory, BattleZone
from equipment.serializers import BattleZoneModelSerializer, EquipmentCategoryModelSerializer, \
    EquipmentModelModelSerializer, EquipmentTypeModelSerializer
from soldier.models import Soldier
from soldier.serializers import SoldierModelSerializer
from statistic.models import LossRecords
from statistic.serializers import LossRecordsSerializer
from django.db.models import F, Sum


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


class LossRecordsViewSet(viewsets.ModelViewSet):
    queryset = LossRecords.objects.select_related(
        'soldier',
        'equipment_type',
        'battle_zone'
    ).all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LossRecordsSerializer


class PaymentByZoneAPI(APIView):
    def get(self, request):
        stats = LossRecords.objects.values('battle_zone__name').annotate(
            total=Sum(F('quantity') * F('equipment_type__reward'))
        ).order_by('-total')

        data = {
            'labels': [item['battle_zone__name'] for item in stats],
            'values': [item['total'] for item in stats]
        }
        return Response(data)


class PaymentByEquipmentAPI(APIView):
    def get(self, request):
        stats = LossRecords.objects.values('equipment_type__name').annotate(
            total=Sum(F('quantity') * F('equipment_type__reward'))
        ).order_by('-total')

        data = {
            'labels': [item['equipment_type__name'] for item in stats],
            'values': [item['total'] for item in stats]
        }
        return Response(data)


class PaymentTimelineAPI(APIView):
    def get(self, request):
        stats = LossRecords.objects.values('date').annotate(
            total=Sum(F('quantity') * F('equipment_type__reward'))
        ).order_by('date')

        data = {
            'labels': [item['date'] for item in stats],
            'values': [item['total'] for item in stats]
        }
        return Response(data)