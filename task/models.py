from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=255, blank=False)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(blank=True)
    progress = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", name="tags", blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=255)
