from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from adminapp.models import Conexion, Sql
from adminapp.clases import conectar
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from adminapp.serializers import ServicioSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView 
import json
from rest_framework.response import Response 
from django.urls import reverse_lazy


class SQLCreateView(CreateView):
    model = Sql
    fields = '__all__'
    template_name = "02servicio/nuevo_servicio.html"


# Crea la vista lista servicio.

class SQLListView(ListView):
    model = Sql
    template_name = "02servicio/listar_servicios.html"


class SQLUpdateView(UpdateView):
    model = Sql
    fields = '__all__'
    template_name = "02servicio/nuevo_servicio.html"

class ServicioDeleteView(DeleteView):
    model = Sql
    success_url = reverse_lazy('listar-servicios')


# Crea la vista que permite visualizar el serializar de los servicios.
class ServiciosList(ListAPIView):
    queryset = Sql.objects.all()
    serializer_class = ServicioSerializer

# Crea la vista para cada servicio.


class ServicioList(APIView):
    def post(self):
        pass

    def get(self, request, id_servicio): 
        obj = conectar.Conectar()
        servicio = Sql.objects.get(id=id_servicio)
        conexion = Conexion.objects.get(nombre=servicio.conexion)
        if(id_servicio == 1):
            return ofertaAcademica(self, obj, servicio, conexion)
        if(id_servicio == 2):
            return listaEstudiantes(self, obj, servicio, conexion)
        if(id_servicio == 3):
            return hojaVida(self, obj, servicio, conexion)
        if(id_servicio == 4):
            return consultaNotas(self, obj, servicio, conexion)
        if(id_servicio == 5):
            return consultaMaterias(self, obj, servicio, conexion)
        return Response("Error en el servicio")


# Crea la vista de estudiantes.
def listaEstudiantes(self, obj, servicio, conexion):

    list = obj.ejecutarServicios(conexion.usuario, conexion.contrasena, conexion.ip, str(
        conexion.puerto), conexion.bd, servicio.sql, conexion.motor)

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    print(list)
    for i in list:
        list1.append(i[0])
        list2.append(i[2])
        list3.append(i[3])
        list4.append(i[4])
        list5.append(i[5])
        list6.append(i[6])

    j = 0
    materias = []
    while j < len(list1):
        materias.append({'codigo': list1[j], 'nombres': list2[j], 'apellidos': list3[j],
                         'semestre': list4[j], 'materia': list5[j], 'programa': list6[j]})
        j += 1

    serializer = json.dumps(materias)
    return Response(json.loads(serializer))


def get_dic_from_two_lists(keys, values):
    return {keys[i]: values[i] for i in range(len(keys))}

# Crea la vista de oferta academica.


def ofertaAcademica(self, obj, servicio, conexion):

    list = obj.ejecutarServicios(conexion.usuario, conexion.contrasena, conexion.ip, str(
        conexion.puerto), conexion.bd, servicio.sql, conexion.motor)

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    for i in list:
        list1.append(i[0])
        list2.append(i[1])
        list3.append(i[2])
        list4.append(i[3])
        list5.append(i[4])
        list6.append(i[5])
        list7.append(i[6])
        list8.append(i[7])
        list9.append(i[8])
        list10.append(i[9])
    j = 0
    oferta = []
    while j < len(list1):
        oferta.append({'codigo': list1[j], 'formacion': list2[j], 'titulo': list3[j],                   'lugar': list4[j], 'metodologia': list5[j], 'creditos': list6[j], 'periodicidad': list7[j],
                       'duracion': list8[j], 'jornada': list9[j], 'valor': list10[j]})
        j += 1

    serializer = json.dumps(oferta)
    return Response(json.loads(serializer))

# Crea la vista de hoja de vida.


def hojaVida(self, obj, servicio, conexion):

    list = obj.ejecutarServicios(conexion.usuario, conexion.contrasena, conexion.ip, str(
        conexion.puerto), conexion.bd, servicio.sql, conexion.motor)

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    for i in list:
        list1.append(i[0])
        list2.append(i[1])
        list3.append(i[2])
        list4.append(i[3])
        list5.append(i[4])
        list6.append(i[5])
        list7.append(i[6])
        list8.append(i[7])
    j = 0
    hoja = []
    while j < len(list1):
        hoja.append({'identificacion': list1[j], 'nombres': list2[j], 'apellidos': list3[j],                   'direccion': list4[j], 'telofono': list5[j], 'estado_civil': list6[j], 'email': list7[j],
                     'tipo_sangre': list8[j]})
        j += 1

    serializer = json.dumps(hoja)
    return Response(json.loads(serializer))

# Crea la vistaque permite consultar notas a los estudiantes.


def consultaNotas(self, obj, servicio, conexion):

    list = obj.ejecutarServicios(conexion.usuario, conexion.contrasena, conexion.ip, str(
        conexion.puerto), conexion.bd, servicio.sql, conexion.motor)

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    print(list)
    for i in list:
        list1.append(i[0])
        list2.append(i[1])
        list3.append(i[2])
        list4.append(i[3])
        list5.append(i[4])
        list6.append(i[5])
        list7.append(i[6])

    j = 0
    materias = []
    while j < len(list1):
        materias.append({'codigo_estudiante': list1[j], 'codigo_materia': list2[j],
                         'materia': list5[j], 'nota': list6[j], 'faltas': list7[j]})
        j += 1

    serializer = json.dumps(materias)
    return Response(json.loads(serializer))


# Crea la vista que permite consultar materias.
def consultaMaterias(self, obj, servicio, conexion):

    list = obj.ejecutarServicios(conexion.usuario, conexion.contrasena, conexion.ip, str(
        conexion.puerto), conexion.bd, servicio.sql, conexion.motor)

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []

    for i in list:
        list1.append(i[0])
        list2.append(i[1])
        list3.append(i[2])
        list4.append(i[3])
        list5.append(i[4])
        list6.append(i[5])

    j = 0
    materias = []
    while j < len(list4):
        materias.append({'codigo': list1[j], 'nombres': list2[j], 'tipo': list3[j],
                         'categoria': list4[j],                   'creditos': list5[j], 'programa': list6[j]})
        j += 1

    serializer = json.dumps(materias)
    return Response(json.loads(serializer))
