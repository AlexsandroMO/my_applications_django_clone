"""
URLs Geral
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('task.urls')),
    path('insurance/', include('insurance.urls')),
    path('project_control/', include('project_control.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
