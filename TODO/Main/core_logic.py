from django.db.models import Q, Count
from .forms import TaskForm
from .models import Task
from django.utils import timezone

def get_filter_task(user, progress=-1, tag="_", search=""):
    tasks = user.tasks.all()
    if search:
        tasks = tasks.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )
    if tag != "_":
        tasks = tasks.filter(tags=tag)
    if progress != -1:
        tasks = tasks.filter(progress=progress)
    return tasks

def get_statistical(user):
    tasks = user.tasks

    counts = tasks.aggregate(
    count_0=Count("progress", filter=Q(progress=0)),  
    count_1=Count("progress", filter=Q(progress=1)),
    count_2=Count("progress", filter=Q(progress=2)),
    count_3=Count("progress", filter=Q(progress=3)),
    count_4=Count("progress", filter=Q(progress=4)),
    )
    return counts

def updateTask(request):
    task_id = request.GET.get("id") if request.method == "GET" else request.POST.get("id")
    
    try:
        task = Task.objects.get(id=task_id, author=request.user)
    except Task.DoesNotExist:
        return False 

    if request.method == "GET":
        return TaskForm(instance=task)
    
    elif request.method == "POST":
        form = TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return True
        return False
    return None

def createTask(request):
    if request.method == "GET":
        return TaskForm()
    
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return True
        return False
    return None

def changeState(request):
    task_id = request.POST.get("id")
    state = request.POST.get("state")
    
    try:
        task = Task.objects.get(id=task_id, author=request.user)
        task.progress = state
        task.save()
    except Task.DoesNotExist:
        pass 

def deleteTask(request):
    task_id = request.POST.get("id")
    
    try:
        task = Task.objects.get(id=task_id, author=request.user)
        task.delete()
    except Task.DoesNotExist:
        pass 

def check_overdue_tasks(user):
    now = timezone.now()
    overdue = user.tasks.filter(
        deadline__lt=now,  
        deadline__isnull=False,
        progress__in=[0, 1]  
    )
    updated = overdue.update(progress=3)
    return updated  