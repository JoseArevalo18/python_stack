from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('random_word/', views.index),
    path('random_word/reset', views.reset),
]