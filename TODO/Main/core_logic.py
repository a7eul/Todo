from . import models, forms
from django.db.models import Q, Count, QuerySet
from django.contrib.auth import get_user_model
from .models import Task
from .forms import Task_form

def get_filter_task(user: models.User, progress = -1, tag = "_"):
    tasks = user.task
    if tag == "_" and progress == -1:
        list_task = tasks.all()
    else:
        list_task = tasks.filter(Q(progress = progress) & Q(tags = tag))
    return list_task

def get_statistical(user):
    tasks = user.task
    counts = tasks.aggregate(   # aggregate и annotate применяються ко всей таблице а не к конкретному объекту
        count_0 = Count("progress", filter=Q(progress = 0)),
        count_1 = Count("progress", filter=Q(progress = 1)),
        count_2 = Count("progress", filter=Q(progress = 2)),
        count_3 = Count("progress", filter=Q(progress = 3)),
        count_4 = Count("progress", filter=Q(progress = 4)),
        )
    # print(tasks[0].count_1) aggregate не дополняет текущую таблицу в отличии от annotate
    return counts

def updateTask(request):
    if request.method == "GET":
        id = request.GET.get("id")
        task = models.Task.objects.get(id = id)
        form = forms.Task_form(instance=task)
        return form
    elif request.method == "POST":
        id = request.GET.get("id")
        task = models.Task.objects.get(id = id)
        form = forms.Task_form(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return True
        return False
    return None

def createTask(request):
    if request.method == "GET":
        form = forms.Task_form()
        return form
    elif request.method == "POST":
        form = forms.Task_form(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return True
        return False
    return None

def changeState(request):
    id = request.POST.get("id")
    state = request.POST.get("state")
    task = models.Task.objects.get(id=id)
    task.progress = state
    task.save()
    
def deleteTask(request):
    id = request.POST.get("id")
    task = models.Task.objects.get(id=id)
    task.delete()