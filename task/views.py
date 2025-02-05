from django.shortcuts import render
from django.views.generic import ListView

from task.models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = "task_list"
    ordering = ['progress', '-datetime']
