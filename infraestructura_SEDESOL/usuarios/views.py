from django.shortcuts import render

def home(request):
    return render(request, 'base.html', {'user': "Nombre de usuario"})

def login(request):
    return render(request, 'login.html')