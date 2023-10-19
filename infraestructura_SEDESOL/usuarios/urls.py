from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('registrar_beneficiario/', views.registrar_beneficiario_calentador, name='registrar_beneficiario'),
    path('beneficiarios/', views.lista_beneficiarios, name='beneficiarios'),
    path('beneficiario/<int:beneficiario_id>/', views.detalle_beneficiario, name='detalle_beneficiario'),
]