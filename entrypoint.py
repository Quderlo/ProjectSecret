import os
import random
from datetime import timedelta

import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Olympics.settings')
django.setup()

from soldier.models import Soldier
from equipment.models import EquipmentModel, EquipmentCategory, EquipmentType, BattleZone

def generate_military_id():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))

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

categories = {}
for category_name in INITIAL_DATA["categories"]:
    cat, created = EquipmentCategory.objects.get_or_create(
        display_name=category_name
    )
    categories[category_name] = cat
    print(f"{'Created' if created else 'Exists'} category: {category_name}")

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

EQUIPMENT_DATA = [
    {"name": "M1A2 Abrams (США)", "model": "Танк", "category": "Наземная техника", "reward": 5000},
    {"name": "Leopard 2A7 (Германия)", "model": "Танк", "category": "Наземная техника", "reward": 4800},
    {"name": "Challenger 3 (Великобритания)", "model": "Танк", "category": "Наземная техника", "reward": 4700},
    {"name": "Leclerc XLR (Франция)", "model": "Танк", "category": "Наземная техника", "reward": 4600},
    {"name": "K2 Black Panther (Южная Корея)", "model": "Танк", "category": "Наземная техника", "reward": 4900},
    {"name": "CV90 MkIV (Швеция)", "model": "БМП", "category": "Наземная техника", "reward": 4000},
    {"name": "Puma IFV (Германия)", "model": "БМП", "category": "Наземная техника", "reward": 4200},
    {"name": "Bradley M2A4 (США)", "model": "Бронетранспортер", "category": "Наземная техника", "reward": 3500},
    {"name": "Boxer IFV (Германия)", "model": "Бронетранспортер", "category": "Наземная техника", "reward": 3600},
    {"name": "Patria AMV (Финляндия)", "model": "Бронетранспортер", "category": "Наземная техника", "reward": 3400},
    {"name": "HIMARS M142 (США)", "model": "РСЗО", "category": "Наземная техника", "reward": 6000},
    {"name": "M270 MLRS (США)", "model": "РСЗО", "category": "Наземная техника", "reward": 6200},
    {"name": "PzH 2000 (Германия)", "model": "САУ", "category": "Наземная техника", "reward": 4500},
    {"name": "CAESAR (Франция)", "model": "САУ", "category": "Наземная техника", "reward": 4300},
    {"name": "Archer Artillery System (Швеция)", "model": "САУ", "category": "Наземная техника", "reward": 4400},
    {"name": "F-35 Lightning II (США)", "model": "Истребитель", "category": "Воздушная техника", "reward": 15000},
    {"name": "F-22 Raptor (США)", "model": "Истребитель", "category": "Воздушная техника", "reward": 18000},
    {"name": "Eurofighter Typhoon (ЕС)", "model": "Истребитель", "category": "Воздушная техника", "reward": 12000},
    {"name": "Dassault Rafale (Франция)", "model": "Истребитель", "category": "Воздушная техника", "reward": 13000},
    {"name": "JAS 39 Gripen E (Швеция)", "model": "Истребитель", "category": "Воздушная техника", "reward": 11000},
    {"name": "B-21 Raider (США)", "model": "Бомбардировщик", "category": "Воздушная техника", "reward": 25000},
    {"name": "B-2 Spirit (США)", "model": "Бомбардировщик", "category": "Воздушная техника", "reward": 24000},
    {"name": "AH-64 Apache (США)", "model": "Вертолет", "category": "Воздушная техника", "reward": 8000},
    {"name": "Tiger HAD (Франция/Германия)", "model": "Вертолет", "category": "Воздушная техника", "reward": 7500},
    {"name": "MQ-9 Reaper (США)", "model": "БПЛА", "category": "Воздушная техника", "reward": 3000},
    {"name": "RQ-4 Global Hawk (США)", "model": "БПЛА", "category": "Воздушная техника", "reward": 5000},
    {"name": "Bayraktar TB2 (Турция)", "model": "БПЛА", "category": "Воздушная техника", "reward": 2800},
    {"name": "Arleigh Burke-class (США)", "model": "Эсминец", "category": "Морская техника", "reward": 20000},
    {"name": "Horizon-class (Франция/Италия)", "model": "Эсминец", "category": "Морская техника", "reward": 19000},
    {"name": "Zumwalt-class (США)", "model": "Эсминец", "category": "Морская техника", "reward": 22000},
    {"name": "Virginia-class (США)", "model": "Подводная лодка", "category": "Морская техника", "reward": 25000},
    {"name": "Astute-class (Великобритания)", "model": "Подводная лодка", "category": "Морская техника", "reward": 23000},
    {"name": "Gerald R. Ford-class (США)", "model": "Авианосец", "category": "Морская техника", "reward": 50000},
    {"name": "Queen Elizabeth-class (Великобритания)", "model": "Авианосец", "category": "Морская техника", "reward": 48000},
    {"name": "FREMM-class (Франция/Италия)", "model": "Фрегат", "category": "Морская техника", "reward": 18000},

    {"name": "Т-14 Армата (Россия)", "model": "Танк", "category": "Наземная техника", "reward": 7000},
    {"name": "Т-90М Прорыв (Россия)", "model": "Танк", "category": "Наземная техника", "reward": 6500},
    {"name": "БМП-3 (Россия)", "model": "Бронетранспортер", "category": "Наземная техника", "reward": 4000},
    {"name": "Искандер-М (Россия)", "model": "РСЗО", "category": "Наземная техника", "reward": 8500},
    {"name": "СУ-57 (Россия)", "model": "Истребитель", "category": "Воздушная техника", "reward": 18000},
    {"name": "МиГ-35 (Россия)", "model": "Истребитель", "category": "Воздушная техника", "reward": 15000},
    {"name": "Ка-52 Аллигатор (Россия)", "model": "Вертолет", "category": "Воздушная техника", "reward": 9500},
    {"name": "Орлан-10 (Россия)", "model": "БПЛА", "category": "Воздушная техника", "reward": 2500},
    {"name": "Проект 22350 Адмирал Горшков (Россия)", "model": "Фрегат", "category": "Морская техника",
     "reward": 22000},
    {"name": "С-400 Триумф (Россия)", "model": "ПВО", "category": "Наземная техника", "reward": 10000},
]

for item in EQUIPMENT_DATA:
    try:
        category = EquipmentCategory.objects.get(display_name=item['category'])
        model = EquipmentModel.objects.get(
            display_name=item['model'],
            category=category
        )
        obj, created = EquipmentType.objects.get_or_create(
            name=item['name'],
            defaults={
                'model': model,
                'reward': item['reward']
            }
        )
        status = "Создано" if created else "Уже существует"
        print(f"{status}: {obj.name}")
    except EquipmentCategory.DoesNotExist:
        print(f"Ошибка: Категория '{item['category']}' не найдена")
    except EquipmentModel.DoesNotExist:
        print(f"Ошибка: Модель '{item['model']}' в категории '{item['category']}' не найдена")

directions = [
    "Южное направление",
    "Западное направление",
    "Восточное направление",
    "Северное направление",
]

for zone_name in directions:
    obj, created = BattleZone.objects.get_or_create(name=zone_name)
    status = "Создано" if created else "Уже существует"
    print(f"{status}: {zone_name}")

    first_names = [
        'Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей',
        'Алексей', 'Артём', 'Илья', 'Кирилл', 'Михаил',
        'Никита', 'Матвей', 'Роман', 'Егор', 'Арсений',
        'Иван', 'Денис', 'Евгений', 'Даниил', 'Тимофей'
    ]

    last_names = [
        'Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Кузнецов',
        'Васильев', 'Попов', 'Соколов', 'Михайлов', 'Новиков',
        'Фёдоров', 'Морозов', 'Волков', 'Алексеев', 'Лебедев',
        'Семёнов', 'Егоров', 'Павлов', 'Козлов', 'Степанов'
    ]

    patronymics = [
        'Александрович', 'Дмитриевич', 'Сергеевич', 'Андреевич',
        'Алексеевич', 'Артёмович', 'Ильич', 'Кириллович', 'Михайлович',
        'Никитич', 'Романович', 'Егорович', 'Иванович', 'Евгеньевич', None
    ]

    units = list(Soldier.Unit.values)
    ranks = list(Soldier.Rank.values)

    for _ in range(30):
        soldier_data = {
            'first_name': random.choice(first_names),
            'last_name': random.choice(last_names),
            'patronymic': random.choice(patronymics),
            'birthday': timezone.now().date() - timedelta(days=random.randint(6570, 12775)),  # 18-35 лет
            'military_id': generate_military_id(),
            'rank': random.choice(ranks),
            'unit': random.choice(units)
        }

        try:
            Soldier.objects.create(**soldier_data)
            print(f"Создан: {soldier_data['last_name']} {soldier_data['first_name']}")
        except Exception as e:
            print(f"Ошибка: {str(e)}")

print("\nInitialization completed!")

