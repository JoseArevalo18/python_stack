from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/',views.addCourse),
    path('courses/destroy/<int:number>',views.deleteCourse)
    ]