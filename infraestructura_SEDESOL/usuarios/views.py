from django.shortcuts import render, redirect
from .forms import BeneficiariosCalentadoresForm
from .models import Beneficiarios_Calentadores
from django.core.paginator import Paginator

def home(request):
    return render(request, 'base.html', {'user': "Nombre de usuario"})

def login(request):
    return render(request, 'login.html')

def registrar_beneficiario_calentador(request):
    if request.method == 'POST':
        form = BeneficiariosCalentadoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiarios')
    else:
        form = BeneficiariosCalentadoresForm()

    return render(request, 'beneficiario_calentador.html', {'form': form})

def lista_beneficiarios(request):
    beneficiarios = Beneficiarios_Calentadores.objects.order_by('id')
    paginator = Paginator(beneficiarios, 6)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    
    return render(request, 'beneficiarios.html', {'beneficiarios': comments_page})

def detalle_beneficiario(request, beneficiario_id):
    beneficiario = Beneficiarios_Calentadores.objects.get(pk=beneficiario_id)
    return render(request, 'detalle_beneficiario.html', {'beneficiario': beneficiario})