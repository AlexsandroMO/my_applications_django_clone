from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_project

urlpatterns = [
    path('home_project/', home_project, name='home-project'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
