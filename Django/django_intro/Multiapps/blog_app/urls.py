from django.urls import path
from . import views 

urlpatterns = [
    path('', views.root),
    path('/', views.index),
    path('/new', views.new),
    path('/create', views.create),
    #path('json/', views.jsonresponse),
    path('/<int:number>', views.show),
    path('/<int:number>/edit', views.edit), 
    path('/<int:number>/delete', views.destroy), 
]