from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='usuarios'),
    path('registrar_usuario', views.registrarUsuario, name='registrar_usuario'),
    path('restablecer/<int:id>', views.restablecerUsuario, name='restablecer_usuario'),
    path('eliminar/<int:id>', views.eliminarUsuario, name='eliminar_usuario'),
    path('perfil/', views.editarPerfil, name='perfil'),
    path('perfil/cambiar_password', views.cambiarContraseña, name='cambiar_password'),
]