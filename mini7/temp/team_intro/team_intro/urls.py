from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import team_intro

app_name = 'team_intro'

urlpatterns = [
    path('admin', admin.site.urls),
    path('', team_intro, name='team_intro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

