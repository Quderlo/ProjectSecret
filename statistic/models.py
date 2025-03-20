from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from equipment.models import EquipmentType, BattleZone
from soldier.models import Soldier


class LossRecords(models.Model):
    soldier = models.ForeignKey(
        Soldier,
        on_delete=models.CASCADE,
        verbose_name="Солдат",
        related_name='loss_records'
    )

    equipment_type = models.ForeignKey(
        EquipmentType,
        on_delete=models.CASCADE,
        verbose_name="Тип техники",
        related_name='loss_records'
    )

    battle_zone = models.ForeignKey(
        BattleZone,
        on_delete=models.CASCADE,
        verbose_name="Зона боевых действий",
        related_name='loss_records'
    )

    date = models.DateField(
        verbose_name="Дата уничтожения",
        default=timezone.now
    )

    quantity = models.PositiveIntegerField(
        verbose_name="Количество уничтоженных единиц",
        default=1
    )

    class Meta:
        verbose_name = 'Запись о потерях'
        verbose_name_plural = 'Записи о потерях'
        ordering = ['-date', 'soldier']

    def __str__(self):
        return (f"{self.soldier} - {self.equipment_type.name} "
                f"({self.quantity} шт.) - {self.date}")

    def clean(self):
        if self.date > timezone.now().date():
            raise ValidationError({'date': 'Дата не может быть в будущем'})

        if self.quantity < 1:
            raise ValidationError({'quantity': 'Количество должно быть не менее 1'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)