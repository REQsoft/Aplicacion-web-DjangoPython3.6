from django.shortcuts import render, redirect
from adminapp.models import Parametrizacion
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView
from .. serializers import ParametrizacionSerializer

# Crea la vista que permite visualizar el serializar de parametrización.    
def listar_parametrizaciones(request):
    parametrizacion = Parametrizacion.objects.all().order_by('id')
    contexto = {'parametrizacion':parametrizacion}
    return render(request, '06parametrizacion/listar_parametrizaciones.html', contexto)

# Crea la vista que permite editar la parametrización.  
class ParametrizacionUpdate(UpdateView):
    model = Parametrizacion
    fields = '__all__'
    def get_success_url(self):
        return reverse('listar-parametrizaciones')

# Crea la vista que permite visualizar la parametrización.  
class ParametrizacionList(ListAPIView):
    queryset = Parametrizacion.objects.all()
    serializer_class = ParametrizacionSerializer