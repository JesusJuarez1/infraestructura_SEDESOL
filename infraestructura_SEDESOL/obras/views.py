from django.shortcuts import render, redirect
from .forms import ObraPublicaForm, FiltroObraPublicaForm
from .models import ObraPublica, EvidenciasObrasPublicas
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def registrar_obra_publica(request):
    if request.method == 'POST':
        form = ObraPublicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obras_publicas')
    else:
        form = ObraPublicaForm()

    return render(request, 'registrar_obra.html', {'form': form})

@staff_member_required
def editar_obra_publica(request, obra_id):
    obra = ObraPublica.objects.get(id=obra_id)
    if request.method == 'POST':
        form = ObraPublicaForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            messages.success(request, 'La obra pública ha sido editada exitosamente.')
            return redirect('obras_publicas')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = ObraPublicaForm(instance=obra)
    
    return render(request, 'editar_obra_publica.html', {'form': form})

@staff_member_required
def eliminar_obra(request, obra_id):
    obra = ObraPublica.objects.get(id=obra_id)
    obra.delete()
    messages.success(request, 'La obra pública ha sido eliminada exitosamente.')
    return redirect('obras_publicas')
    
@login_required
def lista_obras_publicas(request):
    form = FiltroObraPublicaForm()
    # Obtener el usuario actualmente autenticado
    usuario = request.user
    # Verificar si el usuario es un administrador
    if usuario.is_superuser:
        # Si es un administrador, mostrar todos las obras publicas
        obras_publicas = ObraPublica.objects.order_by('id')
    else:
        # Si no es un administrador, mostrar solo las obras publicas donde él sea designado
        obras_publicas = ObraPublica.objects.filter(designado=usuario).order_by('id')
    if request.method == 'POST':
        form = FiltroObraPublicaForm(request.POST)
        municipio = request.POST.get('municipio', None)
        nombre_obra = request.POST.get('nombre_obra', None)
        localidad = request.POST.get('localidad', None)
        folio_mids = request.POST.get('folio_mids', None)
        if municipio:
            obras_publicas = obras_publicas.filter(municipio=municipio)
        if nombre_obra:
            obras_publicas = obras_publicas.filter(nombre_obra__contains=nombre_obra)
        if localidad:
            obras_publicas = obras_publicas.filter(localidad__contains=localidad)
        if folio_mids:
            obras_publicas = obras_publicas.filter(folio_mids__contains=folio_mids)
    paginator = Paginator(obras_publicas, 6)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    status = request.session.pop('status', None)

    context = {
        "obras": comments_page,
        "status": status,
        "form": form
    }
    return render(request, 'obras_publicas.html', context)

@login_required
def completar_obra_publica(request, obra_id):
    obra = ObraPublica.objects.get(pk=obra_id)
    images_proceso = EvidenciasObrasPublicas.objects.filter(obra=obra, es_proceso=True)
    images_completada = EvidenciasObrasPublicas.objects.filter(obra=obra, es_proceso=False)

    if request.method == 'POST':
        # Eliminar imágenes anteriores relacionadas con la obra
        EvidenciasObrasPublicas.objects.filter(obra=obra).delete()

        # Guardar nuevas imágenes
        for image in request.FILES.getlist('images_proceso[]'):
            EvidenciasObrasPublicas.objects.create(obra=obra, imagen=image, es_proceso=True)

        for image in request.FILES.getlist('images_completada[]'):
            EvidenciasObrasPublicas.objects.create(obra=obra, imagen=image, es_proceso=False)

        request.session['status'] = 'Imágenes procesadas exitosamente.'
        return redirect('obras_publicas')
    print(images_proceso)
    return render(request, 'completar_obra_publica.html', {'obra': obra, 'proceso':images_proceso, 'completada': images_completada})

@login_required
def detalles_obra_publica(request, obra_id):
    obra_publica = ObraPublica.objects.get(pk=obra_id)
    imagenes = EvidenciasObrasPublicas.objects.filter(obra=obra_id)
    return render(request, 'detalles_obra_publica.html', {'obra': obra_publica, 'imagenes': imagenes})