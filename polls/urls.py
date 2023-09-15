from django.urls import path
from .views import GetShop,CreateShop,GetCreateShop,DetailUpdateDestroy

urlpatterns = [
    path('getShop/',GetShop.as_view()),
    path('createShop/',CreateShop.as_view()),
    path('getcreateShop/',GetCreateShop.as_view()),
    path('<int:pk>/',DetailUpdateDestroy.as_view())
]