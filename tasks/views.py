from django.views.generic import ListView
from django.http import FileResponse
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = 'tasks'

def download_task_file(request, pk):
    task = Task.objects.get(pk=pk)
    return FileResponse(task.file.open(), as_attachment=True, filename=task.file.name.split('/')[-1])