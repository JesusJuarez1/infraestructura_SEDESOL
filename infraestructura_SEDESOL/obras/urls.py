from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_obras_publicas, name='obras_publicas'),
    path('registrar_obra/', views.registrar_obra_publica, name='registrar_obra_publica'),
    path('detalles/<int:obra_id>/', views.detalles_obra_publica, name='detalles_obra_publica'),
    path('completar_obra_publica/<int:obra_id>/', views.completar_obra_publica, name='completar_obra_publica'),
]