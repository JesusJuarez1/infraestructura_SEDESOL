from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_obras_publicas, name='obras_publicas'),
    path('registrar_obra/', views.registrar_obra_publica, name='registrar_obra_publica'),
    path('editar_obra/<int:obra_id>/', views.editar_obra_publica, name='editar_obra'),
    path('eliminar_obra/<int:obra_id>/', views.eliminar_obra, name='eliminar_obra'),
    path('detalles/<int:obra_id>/', views.detalles_obra_publica, name='detalles_obra_publica'),
    path('completar_obra_publica/<int:obra_id>/', views.completar_obra_publica, name='completar_obra_publica'),
]