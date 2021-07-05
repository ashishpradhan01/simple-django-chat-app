from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:roomname>/', views.room, name='room'),
    path('checkroom', views.checkroom, name='checkroom'),
    path('sendmessage', views.sendmessage, name='sendmessage'),
    path('getmessage/<str:room>', views.getmessage, name='getmessage'),
    path('roomexist/<str:room>', views.roomexist, name='roomexist'),
]
