import re
from rest_framework import serializers
from .models import (
    BattleZone,
    EquipmentCategory,
    EquipmentModel,
    EquipmentType
)


class BattleZoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattleZone
        fields = '__all__'

    def validate_name(self, value):
        if not re.match(r'^[а-яА-ЯёЁ\-\s()"]+$', value):
            raise serializers.ValidationError(
                "Название может содержать только русские буквы, дефисы, пробелы и скобки"
            )
        # Нормализация пробелов
        return ' '.join(value.strip().split()).title()

    def validate(self, data):
        if BattleZone.objects.filter(name=data['name']).exists():
            if self.instance and self.instance.name == data['name']:
                return data
            raise serializers.ValidationError(
                {'name': 'Зона с таким названием уже существует'}
            )
        return data


class EquipmentCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentCategory
        fields = '__all__'

    def validate_display_name(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError(
                "Название категории должно быть не короче 3 символов"
            )
        return value

    def validate(self, data):
        queryset = EquipmentCategory.objects.filter(display_name=data['display_name'])
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError(
                {'display_name': 'Категория с таким названием уже существует'}
            )
        return data


class EquipmentModelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentModel
        fields = '__all__'

    def validate_display_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError(
                "Название модели должно быть не короче 2 символов"
            )
        return value

    def validate(self, data):
        queryset = EquipmentModel.objects.filter(
            display_name=data['display_name'],
            category=data['category']
        )
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError(
                "Модель с таким названием уже существует в этой категории"
            )
        return data


class EquipmentTypeModelSerializer(serializers.ModelSerializer):
    # Добавляем дополнительные поля для отображения
    model_display = serializers.CharField(
        source='model.display_name',
        read_only=True,
        help_text="Название модели техники"
    )

    category_display = serializers.CharField(
        source='model.category.display_name',
        read_only=True,
        help_text="Категория техники"
    )

    class Meta:
        model = EquipmentType
        fields = [
            'id',
            'name',
            'model',
            'model_display',
            'category_display',
            'reward',
        ]
        extra_kwargs = {
            'model': {'write_only': True}  # Прячем исходное поле model в выводе
        }

    def validate_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError(
                "Название типа должно быть не короче 2 символов"
            )
        return value

    def validate(self, data):
        # Проверка уникальности имени
        queryset = EquipmentType.objects.filter(name=data.get('name'))
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError(
                {'name': 'Тип техники с таким названием уже существует'}
            )

        # Проверка соответствия категории (если модель передана в данных)
        if 'model' in data:
            model = data['model']
            if model.category != self.instance.model.category if self.instance else model.category:
                raise serializers.ValidationError(
                    {'model': 'Несоответствие категории модели'}
                )

        return data