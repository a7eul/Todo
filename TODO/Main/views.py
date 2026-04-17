from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models, core_logic
from .models import Task

@login_required
def main(request):
    core_logic.check_overdue_tasks(request.user)

    search_query = request.GET.get("search", "")
    tasks = core_logic.get_filter_task(
        request.user, 
        search=search_query 
    )
    statistic = core_logic.get_statistical(request.user)
    return render(request, "Main/index.html", {
        "tasks": tasks,
        "statistic": statistic,
        "search_query": search_query, 
    })

@login_required
def create(request):
    result = core_logic.createTask(request)
    if result is True:
        return redirect("main") 
    return render(request, "Main/createTask.html", {"form": result})

@login_required
def update(request):
    result = core_logic.updateTask(request)
    if result is True:
        return redirect("main")
    return render(request, "Main/updateTask.html", {"form": result})

@login_required
@login_required
def change_state(request):
    
    if request.method == "POST":
        task_id = request.POST.get("id")
        state = request.POST.get("state")
        try:
            task = Task.objects.get(id=task_id, author=request.user)
            old_progress = task.progress
            task.progress = int(state)
            task.save()
            
            print(f"Задача '{task.name}' изменена с {old_progress} на {state}")
        except Task.DoesNotExist:
            print(f"Задача с id={task_id} не найдена или не принадлежит пользователю")
        except Exception as e:
            print(f"ОШИБКА: {e}")
    return redirect("main")

@login_required
def filter_tasks(request):
    tag = request.POST.get("tag")
    state = request.POST.get("state")
    search = request.POST.get("search", "")  
    list_task = core_logic.get_filter_task(
        user=request.user, 
        progress=state, 
        tag=tag,
        search=search  
    )
    statistic = core_logic.get_statistical(request.user)
    return render(request, "Main/index.html", {
        "tasks": list_task,
        "statistic": statistic,
        "search_query": search,  
    })

@login_required
def delete_task(request):  
    core_logic.deleteTask(request)
    return redirect("main")