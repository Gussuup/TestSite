from django.forms import ModelForm, TextInput, Textarea
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name',
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a description',
            }),
        }
