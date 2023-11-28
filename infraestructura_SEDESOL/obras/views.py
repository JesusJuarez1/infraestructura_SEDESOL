from django.shortcuts import render, redirect
from .forms import ObraPublicaForm
from .models import ObraPublica, EvidenciasObrasPublicas
from django.core.paginator import Paginator
from django.http import JsonResponse
import os
from django.conf import settings

def registrar_obra_publica(request):
    if request.method == 'POST':
        form = ObraPublicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obras_publicas')
    else:
        form = ObraPublicaForm()

    return render(request, 'registrar_obra.html', {'form': form})

def lista_obras_publicas(request):
    obras_publicas = ObraPublica.objects.order_by('id')
    paginator = Paginator(obras_publicas, 6)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    status = request.session.pop('status', None)
    
    return render(request, 'obras_publicas.html', {'obras': comments_page, 'status': status})


def completar_obra_publica(request, obra_id):
    obra = ObraPublica.objects.get(pk=obra_id)
    if request.method == 'POST':
        images_proceso = request.FILES.getlist('images_proceso[]')
        images_completada = request.FILES.getlist('images_completada[]')

        for image in images_proceso:
            EvidenciasObrasPublicas.objects.create(obra=obra, imagen=image, es_proceso=True)

        for image in images_completada:
            EvidenciasObrasPublicas.objects.create(obra=obra, imagen=image, es_proceso=False)

        request.session['status'] = 'Imágenes procesadas exitosamente.'
        return redirect('obras_publicas')
    
    return render(request, 'completar_obra_publica.html', {'obra': obra})

def detalles_obra_publica(request, obra_id):
    obra_publica = ObraPublica.objects.get(pk=obra_id)
    return render(request, 'detalles_obra_publica.html', {'obra_publica': obra_publica})