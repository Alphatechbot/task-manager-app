from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('update/<int:id>/', views.todoUpdate, name='update'),
    path('delete/<int:id>/', views.todoDelete, name='delete'),

    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('register/', views.registerview, name='register'),
]
