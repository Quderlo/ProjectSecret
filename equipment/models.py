from django.db import models


class BattleZone(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Зона боевых действий",
        help_text='Фронт/направление например "Курское направление"',
    )

    class Meta:
        verbose_name = 'Фронт'
        verbose_name_plural = 'Направления'


    def __str__(self):
        return self.name

class EquipmentCategory(models.Model):
    display_name = models.CharField(max_length=100, verbose_name="Отображаемое название")

    class Meta:
        verbose_name = 'Категория техники'
        verbose_name_plural = 'Категории техники'

    def __str__(self):
        return self.display_name

class EquipmentModel(models.Model):
    display_name = models.CharField(max_length=100, verbose_name="Отображаемое название")
    category = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'

    def __str__(self):
        return self.display_name

class EquipmentType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Наименование техники")
    model = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE, verbose_name="Модель техники")

    class Meta:
        verbose_name = 'Тип техники'
        verbose_name_plural = 'Тип техники'

    def __str__(self):
        return f"{self.model.category.display_name} | {self.model.display_name} | {self.name}"
