from django import forms
from . import models

class TaskForm(forms.ModelForm):  
    class Meta:
        model = models.Task
        fields = ["name", "description", "tags", "deadline"]  

        labels = {
            "name": "Название задачи",
            "description": "Описание",
            "tags": "Категория",
        }

        help_texts = {
            "name": "",  
            "description": "",
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите название"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Детали задачи"}),
            "tags": forms.Select(attrs={"class": "form-select"}),
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local",  "class": "form-control"
            }),
        }