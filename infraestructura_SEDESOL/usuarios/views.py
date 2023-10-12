from django.shortcuts import render, redirect
from .forms import BeneficiarioCalentadorForm

def home(request):
    return render(request, 'base.html', {'user': "Nombre de usuario"})

def login(request):
    return render(request, 'login.html')

def registrar_beneficiario_calentador(request):
    if request.method == 'POST':
        form = BeneficiarioCalentadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = BeneficiarioCalentadorForm()

    return render(request, 'beneficiario_calentador.html', {'form': form})