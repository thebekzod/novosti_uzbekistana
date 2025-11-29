# novosti/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),  # ваше приложение с новостями
    path('accounts/', include('django.contrib.auth.urls')),  # логин/логаут и т.д.
]
