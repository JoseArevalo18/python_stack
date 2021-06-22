
from django.urls import path     
from . import views

urlpatterns = [
    path('/', views.perrito),
    path('/nuevo', views.index)
]