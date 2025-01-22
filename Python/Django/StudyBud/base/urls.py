from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room_page/<str:pk>/', views.room, name="room"),
    path('create_room/', views.create_room, name="create-room"),
    path('update_room/<str:pk>/', views.update_room, name="update-room"),
    path('delete_room/<str:pk>/', views.delete_room, name="delete-room"),

]
