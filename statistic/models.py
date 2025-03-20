from django.db import models

from soldier.models import Soldier


# Create your models here.
class LossRecord(models.Model):
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата",
    )

    battle_zone = models.ForeignKey(
        BattleZone,
        on_delete=models.CASCADE,
        verbose_name="Боевой участок",
    )

    equipment_type = models.ForeignKey(
        EquipmentType,
        on_delete=models.CASCADE,
        verbose_name="Тип техники"
    )

    destroyed_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество уничтожено"
    )

    soldier = models.ForeignKey(
        Soldier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Боец",
    )



