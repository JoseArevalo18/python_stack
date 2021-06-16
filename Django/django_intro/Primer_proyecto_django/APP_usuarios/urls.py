from django.http.response import JsonResponse
from django.urls import path     
from . import views

app_name = 'blogs'

urlpatterns = [
    path('users/register', views.newreg),
    path('users/login', views.loginfunc),
    path('users/new', views.newreg),
    path('users', views.index),
]