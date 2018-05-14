from django.shortcuts import render, redirect
from adminapp.models import Localizacion
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView
from .. serializers import LocalizacionSerializer

# Crea la vista formulario nuevo georreferenciación.


def crear_localizacion(request):
    if request.method == 'POST':
        form = LocalizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-localizaciones')
    else:
        form = LocalizacionForm()
        return render(request, '05georeferenciacion/nueva_localizacion.html', {'form': form})

# Crea la vista lista georreferenciación.


def listar_localizaciones(request):
    localizacion = Localizacion.objects.all().order_by('id')
    contexto = {'localizacion': localizacion}
    return render(request, '05georeferenciacion/listar_localizaciones.html', contexto)

# Crea la vista editar georreferenciación.


def editar_localizacion(request, id_localizacion):
    localizacion = Localizacion.objects.get(id=id_localizacion)
    if request.method == 'GET':
        form = LocalizacionForm(instance=localizacion)
    else:
        form = LocalizacionForm(request.POST, instance=localizacion)
        if form.is_valid():
            form.save()
        return redirect('principal:localizacion_listar')
    return render(request, '05vistas/localizacion/localizacion_new.html', {'form': form})

# Crea la vista eliminar georreferenciación.


def eliminar_localizacion(request, id_localizacion):
    localizacion = Localizacion.objects.get(id=id_localizacion)
    if request.method == 'POST':
        localizacion.delete()
        return redirect('principal:localizacion_listar')
    return render(request, '05vistas/localizacion/localizacion_delete.html', {'localizacion': localizacion})

# Crea la vista que permite visualizar el serializar de locaclización.


class LocalizacionList(ListAPIView):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer
