from django import forms
from django.contrib.auth import get_user_model

from task.models import Task


class TaskForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
