from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.main, name="main"),
    path("main/create/", views.create, name="create"),
    path("main/update/", views.update, name="update"),
    path("main/changeState/", views.change_state, name="state"),  
    path("main/filter/", views.filter_tasks, name="filter"),    
    path("main/delete/", views.delete_task, name="delete"),      
    path("main/calendar/", views.calendar_view, name="calendar"),
]