from django.shortcuts import render, redirect
from adminapp.models import Parametrizacion
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from rest_framework.generics import ListAPIView
from .. serializers import ParametrizacionSerializer

# Crea la vista que permite visualizar el serializar de parametrización.    

class ParametrizacionCreateView(CreateView):
    model = Parametrizacion
    fields = '__all__'
    template_name = "06parametrizacion/nueva_parametrizacion.html"


class ParametrizacionListView(ListView):
    model = Parametrizacion
    template_name = "06parametrizacion/listar_parametrizaciones.html"



# Crea la vista que permite editar la parametrización.  
class ParametrizacionUpdate(UpdateView):
    model = Parametrizacion
    fields = '__all__'
    template_name = "06parametrizacion/nueva_parametrizacion.html"


class ParametrizacionDeleteView(DeleteView):
    model = Parametrizacion
    success_url = reverse_lazy('listar-parametrizaciones')


# Crea la vista que permite visualizar la parametrización.  
class ParametrizacionList(ListAPIView):
    queryset = Parametrizacion.objects.all()
    serializer_class = ParametrizacionSerializer