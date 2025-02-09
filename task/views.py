from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View

from task.forms import TaskForm
from task.models import Task, Tag


class TriggerTaskView(View):
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.progress = not task.progress
        task.save()
        return redirect("task:home")


class TaskListView(ListView):
    model = Task
    context_object_name = "task_list"
    ordering = ['progress', '-datetime']


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:home")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task:home")


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag")