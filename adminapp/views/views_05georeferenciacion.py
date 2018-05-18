from django.shortcuts import render, redirect
from adminapp.models import Localizacion
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from rest_framework.generics import ListAPIView
from .. serializers import LocalizacionSerializer

# Crea la vista formulario nuevo georreferenciación.


class LocalizacionCreateView(CreateView):
    model = Localizacion
    fields = '__all__'
    template_name = "05georeferenciacion/nueva_localizacion.html"


# Crea la vista lista georreferenciación.



class LocalizacionListView(ListView):
    model = Localizacion
    template_name = "05georeferenciacion/listar_localizaciones.html"


# Crea la vista editar georreferenciación.



class LocalizacionUpdateView(UpdateView):
    model = Localizacion
    fields = '__all__'
    template_name = "05georeferenciacion/nueva_localizacion.html"


# Crea la vista eliminar georreferenciación.



class LocalizacionDeleteView(DeleteView):
    model = Localizacion
    success_url = reverse_lazy('listar-localizaciones')


# Crea la vista que permite visualizar el serializar de locaclización.


class LocalizacionList(ListAPIView):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer
