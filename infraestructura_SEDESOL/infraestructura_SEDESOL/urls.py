"""
URL configuration for infraestructura_SEDESOL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('infraestructura_sedesol/admin/', admin.site.urls),
    path('infraestructura_sedesol/usuarios/', include('usuarios.urls')),
    path('infraestructura_sedesol/beneficiarios/', include('beneficiarios.urls')),
    path('infraestructura_sedesol/obras_publicas/', include('obras.urls')),
    path('infraestructura_sedesol/home/', include('home.urls')),
    path('infraestructura_sedesol/authentication/', include('authentication.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
