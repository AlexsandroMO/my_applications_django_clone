from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_insurance

urlpatterns = [
    path('home_insurance/', home_insurance, name='home-insurance'),
    #path('home_insurance/', home_insurance.as_view(), name='home-insurance'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



