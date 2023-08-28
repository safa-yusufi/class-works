from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('images/', views.images, name='members'),
    path('chat/', views.chat, name='members'),
    path('videos/', views.videos, name='members'),
    path('maps/', views.maps, name='members'),
    path('news/', views.news, name='news'),
]