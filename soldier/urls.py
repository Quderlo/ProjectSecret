from django.urls import path

from soldier import views

urlpatterns = [
    path('soldiers-list/', views.SoldierListView.as_view(), name='temp-soldier-list'),
]