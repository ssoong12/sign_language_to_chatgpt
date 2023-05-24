# blog/urls.py
from django.urls import path
from . import views

app_name = 'chatgpt'
urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('chat2', views.chat2, name='chat2'),
    path('signlanguagetochatgpt/', views.index2, name='index2'),
]
