import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Olympics.settings')
django.setup()

from equipment.models import EquipmentModel, EquipmentCategory

INITIAL_DATA = {
    "categories": [
        "Наземная техника",
        "Воздушная техника",
        "Морская техника",
        "Космическая техника",
        "Неопределенная категория",
    ],
    "models": [
        ("Неопределенная модель", "Неопределенная категория"),
        ("БМП", "Наземная техника"),
        ("Танк", "Наземная техника"),
        ("Бронетранспортер", "Наземная техника"),
        ("САУ", "Наземная техника"),
        ("РСЗО", "Наземная техника"),
        ("Истребитель", "Воздушная техника"),
        ("Бомбардировщик", "Воздушная техника"),
        ("Штурмовик", "Воздушная техника"),
        ("БПЛА", "Воздушная техника"),
        ("Квадрокоптер", "Воздушная техника"),
        ("Вертолет", "Воздушная техника"),
        ("Эсминец", "Морская техника"),
        ("Подводная лодка", "Морская техника"),
        ("Авианосец", "Морская техника"),
        ("Фрегат", "Морская техника"),
        ("Корвет", "Морская техника"),
    ]
}

# Создаем категории
categories = {}
for category_name in INITIAL_DATA["categories"]:
    cat, created = EquipmentCategory.objects.get_or_create(
        display_name=category_name
    )
    categories[category_name] = cat
    print(f"{'Created' if created else 'Exists'} category: {category_name}")

# Создаем модели
for model_name, category_name in INITIAL_DATA["models"]:
    try:
        category = categories[category_name]
        model, created = EquipmentModel.objects.get_or_create(
            display_name=model_name,
            category=category
        )
        status = "Created" if created else "Exists"
        print(f"{status} model: {model_name} ({category_name})")
    except KeyError:
        print(f"ERROR: Category '{category_name}' not found for model '{model_name}'")

print("\nInitialization completed!")