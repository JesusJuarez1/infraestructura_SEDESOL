from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_beneficiarios, name='beneficiarios'),
    path('registrar_beneficiario/', views.registrar_beneficiario_calentador, name='registrar_beneficiario'),
    path('detalles/<int:beneficiario_id>/', views.detalles_beneficiario, name='detalles_beneficiario'),
    path('completar_obra/<int:beneficiario_id>/', views.completar_obra, name='completar_obra'),
]