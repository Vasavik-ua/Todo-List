from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from task.models import Task, Tag


def trigger_task_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.progress:
        task.progress = False
    else:
        task.progress = True
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
    fields = "__all__"
    success_url = reverse_lazy("task:home")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
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