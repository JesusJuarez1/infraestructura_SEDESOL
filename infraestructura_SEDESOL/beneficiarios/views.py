from django.shortcuts import render, redirect
from .forms import BeneficiarioCalentadorForm
from .models import BeneficiarioCalentador
from django.core.paginator import Paginator

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
    
    return render(request, 'beneficiarios.html', {'beneficiarios': comments_page})

def detalle_beneficiario(request, beneficiario_id):
    beneficiario = BeneficiarioCalentador.objects.get(pk=beneficiario_id)
    return render(request, 'detalle_beneficiario.html', {'beneficiario': beneficiario})