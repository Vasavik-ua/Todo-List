from django.urls import path

from task.views import TaskListView, TaskDeleteView, TaskUpdateView, TaskCreateView, TagListView, TagUpdateView, \
    TagCreateView, TagDeleteView, TriggerTaskView

urlpatterns = [
    path("", TaskListView.as_view(), name='home'),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name='task-delete'),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name='task-update'),
    path("task/create/", TaskCreateView.as_view(), name='task-create'),
    path("tags/", TagListView.as_view(), name='tag'),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(), name='tag_update'),
    path("tag/create/", TagCreateView.as_view(), name='tag_create'),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(), name='tag_delete'),
    path("task/trigger/<int:pk>/", TriggerTaskView.as_view(), name='trigger_task')
]

app_name = "task"
