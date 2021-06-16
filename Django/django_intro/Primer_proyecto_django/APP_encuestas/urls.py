from django.http.response import JsonResponse
from django.urls import path     
from . import views
urlpatterns = [
    path('/', views.root),
    path('/nuevo', views.index)
]