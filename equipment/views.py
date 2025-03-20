from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class BattleZoneListView(TemplateView):
    template_name = 'equipment/temp_battlezone_list.html'

class EquipmentTypeListView(TemplateView):
    template_name = 'equipment/temp_equipmenttype_list.html'