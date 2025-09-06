from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.beauty.urls')),  # API
    path('', include('apps.beauty.front_urls')),  # HTML-шаблоны

    # Если хочешь открыть base.html сразу на корне,
    # то можно прописать это в front_urls.py (см. ниже)
]
