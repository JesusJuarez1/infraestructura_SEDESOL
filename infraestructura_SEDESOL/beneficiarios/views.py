from django.shortcuts import render, redirect
from .forms import BeneficiarioCalentadorForm
from .models import BeneficiarioCalentador, EvidenciasCalentadores
from django.core.paginator import Paginator
from django.http import JsonResponse
import os
from django.conf import settings

def registrar_beneficiario_calentador(request):
    if request.method == 'POST':
        form = BeneficiarioCalentadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiarios')
    else:
        form = BeneficiarioCalentadorForm()

    return render(request, 'beneficiario_calentador.html', {'form': form})

def lista_beneficiarios(request):
    beneficiarios = BeneficiarioCalentador.objects.order_by('id')
    paginator = Paginator(beneficiarios, 6)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    status = request.session.pop('status', None)
    
    return render(request, 'beneficiarios.html', {'beneficiarios': comments_page, 'status': status})


def completar_obra(request, beneficiario_id):
    beneficiario = BeneficiarioCalentador.objects.get(pk=beneficiario_id)
    if request.method == 'POST':
        images_proceso = request.FILES.getlist('images_proceso[]')
        images_completada = request.FILES.getlist('images_completada[]')

        for image in images_proceso:
            EvidenciasCalentadores.objects.create(beneficiario=beneficiario, imagen=image, es_proceso=True)

        for image in images_completada:
            EvidenciasCalentadores.objects.create(beneficiario=beneficiario, imagen=image, es_proceso=False)

        request.session['status'] = 'Imágenes procesadas exitosamente.'
        return redirect('beneficiarios')
    
    return render(request, 'completar_obra.html', {'beneficiario': beneficiario})

def detalle_beneficiario(request, beneficiario_id):
    beneficiario = BeneficiarioCalentador.objects.get(pk=beneficiario_id)
    return render(request, 'detalle_beneficiario.html', {'beneficiario': beneficiario})