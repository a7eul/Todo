from django.db.models import Q, Count
from django.contrib.auth import get_user_model
from .models import Task
from .forms import Task_form

User = get_user_model()

def get_filter_tasks(user: User, progress: int = 0, tag: str = "my_tasks"):
    return Task.objects.filter(author=user, progress=progress, tags=tag)

def get_statistical(user: User) -> dict:
    counts = Task.objects.filter(author=user).aggregate(
        count_0=Count("progress", filter=Q(progress=0)),
        count_1=Count("progress", filter=Q(progress=1)),
        count_2=Count("progress", filter=Q(progress=2)),
        count_3=Count("progress", filter=Q(progress=3)),
        count_4=Count("progress", filter=Q(progress=4)),
    )
    return counts

def updateTask(request):
    task_id = request.GET.get("id") or request.POST.get("id")
    if not task_id:
        return None
    
    task = Task.objects.get(id=task_id, author=request.user)
    
    if request.method == "GET":
        return Task_form(instance=task)
        
    elif request.method == "POST":
       
        form = Task_form(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return True
        return False
        
    return None

def createTask(request):
    if request.method == "GET":
        return Task_form()
        
    elif request.method == "POST":
        form = Task_form(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return True
        return False
        
    return None