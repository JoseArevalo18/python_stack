from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	 
    path('books/<int:number>',views.book),
    path('authors/',views.authorIndex),
    path('authors/<int:number>',views.author),
]