from . import models
from django.db.models import Q, Count, QuerySet

def filter_task(progress = 0, tag = "my_tasks"):
    list_task = models.Task.objects.filter(Q(progress = progress) & Q(tag = tag))
    return list_task

def get_statistical(user: QuerySet):
    tasks = user.prefetch_related("task").get(id=2)
    counts = tasks.task.aggregate(   # aggregate и annotate применяються ко всей таблице а не к конкретному объекту
        count_0 = Count("progress", filter=Q(progress = 0)),
        count_1 = Count("progress", filter=Q(progress = 1)),
        count_2 = Count("progress", filter=Q(progress = 2)),
        count_3 = Count("progress", filter=Q(progress = 3)),
        count_4 = Count("progress", filter=Q(progress = 4)),
        )
    # print(tasks[0].count_1) aggregate не дополняет текущую таблицу в отличии от annotate
    return counts


def readTasks(progress=0,tag="my_tasks"):
    tasks = filter_task
    return tasks

def updateTask(request,id):
    if request.method == "GET": 
        id  = request.GET.get("id")
        task = models.Task.objects.get(id=id)
        form = forms.Task_form(instanse=task)
        return form
    elif request.method == "POST":
        form = forms.Task_form(data=request)
        if form.is_valid():
            form.save()
            return True
        return False
    return None

