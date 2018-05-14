from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from adminapp.models import Conexion
from .. clases.conectar import Conectar
from django.urls import reverse_lazy

# Create your views here.


class ConexionCreateView(CreateView):
    model = Conexion
    fields = '__all__'
    template_name = "01conexion/nueva_conexion.html"


class ConexionUpdateView(UpdateView):
    model = Conexion
    fields = '__all__'
    template_name = "01conexion/nueva_conexion.html"


class ConexionListView(ListView):
    model = Conexion
    template_name = "01conexion/listar_conexiones.html"


class ConexionDeleteView(DeleteView):
    model = Conexion
    template_name = "01conexion/eliminar_conexion.html"
    success_url = reverse_lazy('listar-conexiones')


# Crear la vista para listar las base de datos con los parametros ingresados en el ssitema.


def listar_bd(request):
    global bds
    motor = request.POST['motor']
    obj = Conectar()
    if motor == 'postgres':
        bds = obj.conectarPostgres(
            request.POST['usuario'], request.POST['contrasena'], request.POST['ip'], request.POST['puerto'])
    elif motor == 'mysql':
        bds = obj.conectarMysql(
            request.POST['usuario'], request.POST['contrasena'], request.POST['ip'], request.POST['puerto'])
    context = {'object_list': bds}
    return render(request, '01conexion/listar_bd.html', context)
