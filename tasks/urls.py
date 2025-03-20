from django.urls import path
from .views import TaskListView, download_task_file

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/download/', download_task_file, name='task-download'),
]