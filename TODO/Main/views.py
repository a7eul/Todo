from django.shortcuts import render, redirect
from . import forms, models, core_logic


def main(request):
    tasks = []
    statistic = core_logic.get_statistical(request.user)
    if isinstance(request.user, models.User):
        tasks = core_logic.get_filter_task(request.user)
    data = {
        "tasks":tasks,
        "statistic":statistic,
    }
    return render(request, "Main/index.html", data)

            
def create(request):
    form = core_logic.createTask(request)
    if form==True:
        return redirect("main")
    else:
        return render(request, "Main/createTask.html", {"form":form})

def update(request):
    form = core_logic.updateTask(request)
    if form:
        return redirect("main")
    else:
        return render(request, "", {"form":form})