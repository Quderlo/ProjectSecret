from django.urls import path

from statistic import views

urlpatterns = [
    path('lossrecords-list/', views.LossRecordsListView.as_view(), name='temp-lossrecords-list'),
    path('stats-payments/', views.PaymentStatsView.as_view(), name='payment-stats'),
    path('report-form/', views.ReportView.as_view(), name='report-form'),
]