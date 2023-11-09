from django.urls import reverse_lazy
from django.views.generic import ListView, RedirectView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = ['date_task_added']
    
class CreateTaskView(CreateView):
    model = Task
    fields = ['task_name']

class UpdateTaskView(UpdateView):
    model = Task
    fields = ['task_name', 'task_complete']

class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')