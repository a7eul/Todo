from django.urls import path
from .models import User, Task
from .core_logic import get_statistical
from django.http import JsonResponse

def test(request):
    user = User.objects
    stat = get_statistical(user)
    return JsonResponse(stat)



urlpatterns = [
    path("test/", test),
]
