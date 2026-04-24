from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from calendar import monthrange
from .models import Task
from . import core_logic
from django.contrib.auth import logout
from .forms import TaskForm

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

def updateTask(request):
    task_id = request.POST.get("id") or request.GET.get("id")

    if not task_id:
        return False
    
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
    
@login_required
def calendar_view(request):
    year = request.GET.get('year', timezone.now().year)
    month = request.GET.get('month', timezone.now().month)
    
    try:
        year = int(year)
        month = int(month)
    except (ValueError, TypeError):
        year = timezone.now().year
        month = timezone.now().month
    
    tasks = Task.objects.filter(
        author=request.user,
        deadline__isnull=False,
        deadline__year=year,
        deadline__month=month
    ).order_by('deadline')
    
    first_day, num_days = monthrange(year, month)
    
    calendar_days = []
    current_day = 1
    
    for _ in range(first_day):
        calendar_days.append(None)
    
    while current_day <= num_days:
        day_tasks = [task for task in tasks if task.deadline.day == current_day]
        calendar_days.append({
            'day': current_day,
            'tasks': day_tasks,
            'is_today': (current_day == timezone.now().day and 
                        month == timezone.now().month and 
                        year == timezone.now().year)
        })
        current_day += 1
    
    month_names = [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ]
    
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year
    
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    
    context = {
        'year': year,
        'month': month,
        'month_name': month_names[month - 1],
        'calendar_days': calendar_days,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
    }
    
    return render(request, 'Main/calendar.html', context)

@login_required
def user_logout(request):
    logout(request)  
    return redirect("enter")