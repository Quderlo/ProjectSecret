from django.utils import timezone
from rest_framework import serializers
from .models import LossRecords


class LossRecordsSerializer(serializers.ModelSerializer):
    soldier_name = serializers.CharField(
        source='soldier',
        read_only=True,
        help_text="Фамилия солдата"
    )

    equipment_name = serializers.CharField(
        source='equipment_type.name',
        read_only=True,
        help_text="Название техники"
    )

    battle_zone_name = serializers.CharField(
        source='battle_zone.name',
        read_only=True,
        help_text="Название зоны боевых действий"
    )

    sum_award = serializers.SerializerMethodField(
        help_text="Сумма выплаты"
    )

    class Meta:
        model = LossRecords
        fields = [
            'id',
            'soldier',
            'soldier_name',
            'equipment_type',
            'equipment_name',
            'battle_zone',
            'battle_zone_name',
            'date',
            'quantity',
            'sum_award'  # Добавлено поле в вывод
        ]
        extra_kwargs = {
            'soldier': {'write_only': True},
            'equipment_type': {'write_only': True},
            'battle_zone': {'write_only': True}
        }

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Количество должно быть не менее 1")
        return value

    def validate_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Дата не может быть в будущем")
        return value

    def get_sum_award(self, obj):
        return obj.quantity * obj.equipment_type.reward

