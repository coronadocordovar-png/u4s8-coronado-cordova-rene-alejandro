from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import connection
from .models import Servicio


def inicio(request):
    info_bd = connection.settings_dict

    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }

    return render(request, 'core/inicio.html', contexto)


@login_required
def servicios(request):
    lista_servicios = Servicio.objects.filter(
        propietario=request.user
    ).order_by('-creado_en', '-id')

    query = request.GET.get('q', '').strip()

    if query:
        lista_servicios = lista_servicios.filter(
            titulo__icontains=query
        )

    paginator = Paginator(lista_servicios, 5)
    pagina = paginator.get_page(request.GET.get('page'))

    contexto = {
        'servicios': pagina,
        'query': query
    }

    return render(request, 'core/servicios.html', contexto)

def contacto(request):
    return render(request, 'core/contacto.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import ServicioForm


@login_required
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.propietario = request.user
            nuevo.save()
            return redirect('servicios')
    else:
        form = ServicioForm()
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo': 'Crear servicio'})


@login_required
def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk, propietario=request.user)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo': 'Editar servicio'})


@login_required
def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk, propietario=request.user)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicios')
    return render(request, 'core/servicio_confirm_delete.html', {'servicio': servicio})


from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Cuenta creada correctamente.')
            return redirect('servicios')
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Sesion iniciada correctamente.')
            return redirect('servicios')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


@login_required
def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Sesion cerrada correctamente.')
        return redirect('login')
    return redirect('servicios')

