from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    class Progress(models.IntegerChoices):
        ACTIVE = 0 , "Активная"
        WORK = 1 , "В процессе"
        COMPLITE = 2 , "Выполнена"
        FALL = 3 , "Провалена"
        POSTPONED = 4 , "Отложена"

    class Tag(models.TextChoices):
        WORK = "work" , "Работа"
        HOME = "home" , "Дом"
        MY_TASKS = "my_tasks" , "Мои задачи"

    name = models.TextField(max_length=42, verbose_name="Имя задачи")
    description = models.TextField(max_length=700, null=True, verbose_name="Описание задачи")
    tags = models.TextField(choices=Tag.choices, null=True, verbose_name="Теги")
    progress = models.IntegerField(choices=Progress.choices, default=0, verbose_name="Прогресс")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор задачи", related_name="task")