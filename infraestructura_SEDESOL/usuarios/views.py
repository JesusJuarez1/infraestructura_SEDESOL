from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.admin.views.decorators import staff_member_required
import random
import string
from .forms import EditUserForm, MyPasswordChangeForm

@login_required
@staff_member_required
def registrarUsuario(request):

    if request.method == 'GET':
        password_temporal = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        request.session['password_temporal'] = password_temporal

        return render(request, 'registro_usuarios.html', {
            'password_temporal': password_temporal,
            'form': UserCreationForm()
        })
    else:
        try:
            
            username = request.POST['username']
            password_temporal = request.session.get('password_temporal')
            is_staff = 'es_administrador' in request.POST
            user = User.objects.create_user(
                username=username,
                password=password_temporal,
                is_staff=is_staff
            )
            del request.session['password_temporal']
            messages.success(request, 'Usuario registrado correctamente.')
            return redirect('usuarios')

        except IntegrityError:
            return render(request, 'registro_usuarios.html', {
                'form': UserCreationForm(),
                'password_temporal': request.session.get('password_temporal'),
                "error": 'El usuario ya existe.'
            })
        except BaseException:
            return render(request, 'registro_usuarios.html', {
                'form': UserCreationForm(),
                'password_temporal': request.session.get('password_temporal'),
                "error": 'Por favor ingrese datos válidos.'
            })
        

@login_required
@staff_member_required
def lista_usuarios(request):
    users = User.objects.all().order_by('-is_superuser', '-is_staff')
    return render(request, 'lista_usuarios.html', {'users': users})

@login_required
@staff_member_required
def restablecerUsuario(request, id):
    user = User.objects.get(id=id)
    password_temporal = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    user.first_name = ''
    user.last_name = ''
    user.email = ''
    user.set_password(password_temporal)
    user.save()
    messages.success(request, 'Usuario restablecido correctamente. La nueva contraseña es: ' + password_temporal)
    return redirect('usuarios') 

@login_required
@staff_member_required
def eliminarUsuario(request, id):
    User.objects.get(id=id).delete()
    return redirect('usuarios')

@login_required
def editarPerfil(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        context = {
            'form': form,
            
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos del usuario actualizados.')
            return render(request, 'perfil.html', context)
    else:
        form = EditUserForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'perfil.html', context)

@login_required
def cambiarContraseña(request):
    if request.method == 'POST':
        form = MyPasswordChangeForm(data=request.POST, user=request.user)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()

            return redirect('login')
        else:
            return render(request, 'cambiar_contra.html', {
                'form': form,
            })
    else:
        form = MyPasswordChangeForm(user=request.user)

    context = {
        'form': form,
    }
    return render(request, 'cambiar_contra.html', context)