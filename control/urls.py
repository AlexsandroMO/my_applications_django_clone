"""
URLs Geral
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.task.urls')),
    path('', include('apps.insurance.urls')),
    path('', include('apps.project_control.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


]
