from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from .. models import Directorio
from rest_framework.generics import ListAPIView 
from .. serializers import DirectorioSerializer

# Crea la vista formulario nuevo directorio.


class DirectorioCreateView(CreateView):
    model = Directorio
    fields= '__all__'
    template_name = "03directorio/nuevo_directorio.html"


# Crea la vista lista directorios.

class DirecotorioListView(ListView):
    model = Directorio
    template_name = "03directorio/listar_directorios.html"


class DirectorioUpdateView(UpdateView):
    model = Directorio
    fields= '__all__'
    template_name = "03directorio/nuevo_directorio.html"



# Crea la vista que permite visualizar el serializar de deirectorio telefónico.

class DirectorioList(ListAPIView):
    queryset = Directorio.objects.all()
    serializer_class = DirectorioSerializer
