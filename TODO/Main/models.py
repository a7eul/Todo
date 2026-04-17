from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Progress(models.IntegerChoices):
        ACTIVE = 0, "Активная"
        WORK = 1, "В процессе"
        COMPLETED = 2, "Выполнена"
        FALL = 3, "Провалена"
        POSTPONED = 4, "Отложена"

    class Tag(models.TextChoices):
        WORK = "work", "Работа"
        HOME = "home", "Дом"
        MY_TASKS = "my_tasks", "Мои задачи"

    name = models.CharField(max_length=42, verbose_name="Имя задачи")
    description = models.TextField(max_length=700, blank=True, default="", verbose_name="Описание задачи")
    tags = models.CharField(max_length=20, choices=Tag.choices, blank=True, default=Tag.MY_TASKS, verbose_name="Тег")
    progress = models.IntegerField(choices=Progress.choices, default=Progress.ACTIVE, verbose_name="Прогресс")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор задачи", related_name="tasks")
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Дедлайн")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-id"]  