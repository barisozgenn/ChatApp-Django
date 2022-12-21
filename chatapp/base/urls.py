from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('rooms/', views.rooms, name="rooms"),
    path('room/<str:pk>/', views.room, name="room"),
    path('users/', views.users, name="users"),
]