from django.shortcuts import render, redirect
from .forms import BeneficiarioCalentadorForm, FiltroBeneficiarioForm
from .models import BeneficiarioCalentador, EvidenciasCalentadores
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def registrar_beneficiario_calentador(request):
    if request.method == 'POST':
        form = BeneficiarioCalentadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiarios')
    else:
        form = BeneficiarioCalentadorForm()

    return render(request, 'beneficiario_calentador.html', {'form': form})

@login_required
def editar_beneficiario_calentador(request, beneficiario_id):
    beneficiario = BeneficiarioCalentador.objects.get(id=beneficiario_id)
    if request.method == 'POST':
        form = BeneficiarioCalentadorForm(request.POST, instance=beneficiario)
        if form.is_valid():
            form.save()
            messages.success(request, 'El beneficiario ha sido editado exitosamente.')
            return redirect('beneficiarios')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = BeneficiarioCalentadorForm(instance=beneficiario)
    
    return render(request, 'editar_beneficiario_calentador.html', {'form': form})

@login_required
def eliminar_beneficiario_calentador(request, beneficiario_id):
    beneficiario = BeneficiarioCalentador.objects.get(id=beneficiario_id)
    beneficiario.delete()
    messages.success(request, 'El beneficiario ha sido eliminado exitosamente.')
    return redirect('beneficiarios')

@login_required
def lista_beneficiarios(request):
    form = FiltroBeneficiarioForm
    # Obtener el usuario actualmente autenticado
    usuario = request.user
    # Verificar si el usuario es un administrador
    if usuario.is_superuser:
        # Si es un administrador, mostrar todos los beneficiarios
        beneficiarios = BeneficiarioCalentador.objects.order_by('id')
    else:
        # Si no es un administrador, mostrar solo los beneficiarios donde él sea designado
        beneficiarios = BeneficiarioCalentador.objects.filter(designado=usuario).order_by('id')
    if request.method == 'POST':
        form = FiltroBeneficiarioForm(request.POST)
        municipio = request.POST.get('municipio', None)
        nombre = request.POST.get('nombre', None)
        localidad = request.POST.get('localidad', None)
        folio_mids = request.POST.get('folio_mids', None)
        if municipio:
            beneficiarios = beneficiarios.filter(municipio=municipio)
        if nombre:
            beneficiarios = beneficiarios.filter(
                Q(apellido_paterno__contains=nombre) |
                Q(apellido_materno__contains=nombre) |
                Q(nombres__contains=nombre)
            )
        if localidad:
            beneficiarios = beneficiarios.filter(localidad__contains=localidad)
        if folio_mids:
            beneficiarios = beneficiarios.filter(folio_mids__contains=folio_mids)
    paginator = Paginator(beneficiarios, 6)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    status = request.session.pop('status', None)
    context = {
        "beneficiarios": comments_page,
        "status": status,
        "form": form
    }
    
    return render(request, 'beneficiarios.html', context)

@login_required
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

@login_required
def detalles_beneficiario(request, beneficiario_id):
    beneficiario = BeneficiarioCalentador.objects.get(pk=beneficiario_id)
    imagenes = EvidenciasCalentadores.objects.filter(beneficiario=beneficiario_id)
    return render(request, 'detalle_beneficiario.html', {'beneficiario': beneficiario, 'imagenes': imagenes})