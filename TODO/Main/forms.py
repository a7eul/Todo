from django import forms
from . import models

class Task_form(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ["name", "description","tags"]

        help_texts = {
            "name": "Введите свое имя",
            "description": "Описание отсутствует",
        }