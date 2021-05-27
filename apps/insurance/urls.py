from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_insurance, ListaCliente, EditSegur, DeleteSegur, DeleteConfirm, NewSegur, VCliente, DB_Atualyze

urlpatterns = [
    path('home_insurance/', home_insurance, name='home-insurance'),
    path('lista_cliente', ListaCliente, name='lista-cliente'),
    path('edite_segur/<int:id>', EditSegur, name='edit-segur'),
    path('delete_segur/<int:id>', DeleteSegur, name='delete-segur'),
    path('delete_confirm/<int:id>', DeleteConfirm, name='delete-confir'),
    path('new_segur', NewSegur, name='new-segur'),
    path('v_cliente', VCliente, name='v-cliente'),
    path('db_atualyze', DB_Atualyze, name='db-atualyze'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



