from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/<int:number>',views.user_page),
    path('user/dashboard', views.dashboard),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('book/book_form', views.book_form),
    path('book/create', views.create_book),
    path('book/<int:number>',views.show_book),
    path('book/add_review',views.add_review),
    path('review/<int:number>/delete',views.delete_review)
]
