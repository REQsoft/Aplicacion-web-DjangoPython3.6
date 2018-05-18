from adminapp.models import Articulo
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from rest_framework.generics import ListAPIView
from .. serializers import ArticuloSerializer


# Vistas Articulos Extraviados
# Crea la vista formulario nuevo articulos extraviados.


class ArticuloCreate(CreateView):
    model = Articulo
    fields = '__all__'
    template_name = '04articulo/nuevo_articulo.html'

# Crea la vista lista articulos extraviados.

class ArticuloListView(ListView):
    model = Articulo
    template_name = "04articulo/listar_articulos.html"

# Crea la vista editar articulos extraviados.


class ArticuloUpdate(UpdateView):
    model = Articulo
    fields = '__all__'
    template_name = "04articulo/nuevo_articulo.html"

# Crea la vista eliminar articulos extraviados.

class ArticuloDeleteView(DeleteView):
    model = Articulo
    succes_url = reverse_lazy('listar-articulos')

# Crea la vista que permite visualizar el serializar de los artículos.

class ArticuloList(ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
