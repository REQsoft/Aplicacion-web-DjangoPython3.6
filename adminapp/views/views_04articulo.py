from django.shortcuts import render, redirect
from adminapp.models import Articulo
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView 
from .. serializers import ArticuloSerializer

# Vistas Articulos Extraviados
# Crea la vista formulario nuevo articulos extraviados.


class ArticuloCreate(CreateView):
    model = Articulo
    fields = '__all__'
    template_name = '04articulo/nuevo_articulo.html'

    def get_success_url(self):
        return reverse('04articulo/listar_articulos.html')

# Crea la vista lista articulos extraviados.

# Crea la vista que permite visualizar el serializar de los artículos.


class ArticuloList(ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


def listar_articulos(request):
    articulo = Articulo.objects.all().order_by('id')
    contexto = {'articulo': articulo}
    return render(request, '04articulo/listar_articulos.html', contexto)

# Crea la vista editar articulos extraviados.


class ArticuloUpdate(UpdateView):
    model = Articulo
    fields = '__all__'

    def get_success_url(self):
        return reverse('04articulo/listar_articulos.html')

# Crea la vista eliminar articulos extraviados.


def articulo_delete(request, id_descripcion):
    articulo = Articulo.objects.get(id=id_descripcion)
    if request.method == 'POST':
        articulo.delete()
        return redirect('04articulo/listar_articulos.html')
    return render(request, '04articulo/listar_articulos.html', {'articulo': articulo})
