from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from adminapp.models import Conexion
from .. clases.conectar import Conectar
from django.urls import reverse_lazy

# Create your views here.

def base_conexion(request):
    return render(request, "01conexion/base.html")

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


def validar_conexion(request):
    motor = request.POST['motor']
    usuario = request.POST['usuario']
    contrasena = request.POST['contrasena']
    puerto = request.POST['puerto']
    ip_servidor = request.POST['ip_servidor']

    cnx = Conectar(usuario,contrasena,puerto,ip_servidor)
    context = {}

    if motor == 'mysql':
        if cnx.validar_conexion_mysql():     
            lista_db = cnx.listar_db_mysql() 
            if lista_db is not None:
                context =  {'object_list':lista_db}
        return render(request, '01conexion/validar_conexion.html', context)
    if motor == 'postgres':
        pass
    if motor == 'oracle':
        pass
    