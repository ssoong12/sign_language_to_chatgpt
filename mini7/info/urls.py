from django.urls import path
from . import views

app_name='info'
urlpatterns = [
    path('', views.picture_view, name='picture'),
    path('image_desc_list/', views.image_desc_list, name='picture'),
]