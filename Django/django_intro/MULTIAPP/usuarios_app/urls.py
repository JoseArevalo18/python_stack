from django.http.response import JsonResponse
from django.urls import path     
from . import views

app_name = 'blogs'

urlpatterns = [
    path('users/new',views.nuevo),
    path('users/login',views.loginf),
    path('users/',views.index),
]