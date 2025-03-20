import re

from django.utils import timezone
from rest_framework import serializers

from soldier.models import Soldier


class SoldierModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soldier
        fields = '__all__'

    def validate(self, data):
        name_regex = r'^[а-яА-ЯёЁ\-\s]+$'
        fields_to_check = ['first_name', 'last_name', 'patronymic']
        for field in fields_to_check:
            value = data.get(field)
            if value:
                if not re.match(name_regex, value):
                    raise serializers.ValidationError(
                        {field: "Допустимы только русские буквы, дефисы и пробелы."}
                    )
                normalized_value = ' '.join(value.strip().split()).title()
                data[field] = normalized_value

        birthday = data.get('birthday')
        if birthday and birthday > timezone.now().date():
            raise serializers.ValidationError(
                {"birthday": "Дата рождения не может быть в будущем."}
            )

        military_id = data.get('military_id')
        if military_id:
            queryset = Soldier.objects.filter(military_id=military_id)
            instance = getattr(self, 'instance', None)
            if instance:
                queryset = queryset.exclude(pk=instance.pk)
            if queryset.exists():
                raise serializers.ValidationError(
                    {"military_id": "Военный билет с таким номером уже существует."}
                )

        return data