from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('registrar_beneficiario/', views.registrar_beneficiario_calentador, name='registrar_beneficiario'),
]