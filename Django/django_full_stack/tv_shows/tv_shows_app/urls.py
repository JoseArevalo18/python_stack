from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayShow),
    path('shows/new',views.index),
    path('shows/create', views.addShow),
    path('shows/',views.displayShow),
    path('shows/<int:number>', views.showInfo),
    path('shows/<int:number>/edit', views.editShow),
    path('shows/update/<int:number>',views.editShow),
    path('shows/<int:number>/delete',views.delete_show),
    path('shows/networks',views.showNetworks)
]