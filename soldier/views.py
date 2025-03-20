from django.views.generic import TemplateView
from rest_framework import viewsets, permissions

from soldier.models import Soldier


class SoldierListView(TemplateView):
    template_name = 'soldier/temp_soldier_list.html'