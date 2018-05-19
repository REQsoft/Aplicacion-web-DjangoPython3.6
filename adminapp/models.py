from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Conexion(models.Model):
    Motores = (
        ('', (('postgres', 'Postgres'),)),
        ('', (('oracle', 'Oracle'),)),
        ('', (('mysql', 'Mysql'),)),)

    # Atributos del modelo conexión
    nombre = models.CharField(max_length=50)
    ip_servidor = models.CharField(max_length=16)
    puerto = models.IntegerField()
    motor = models.CharField(max_length=50, choices=Motores)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50, blank=True)
    nombre_bd = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 
    
    def get_absolute_url(self):
        return reverse('listar-conexiones')

# Atributos sentencia SQL
class Sql(models.Model):
    Rol = (

        ('', (
            ('administrativo', 'Administrativo'),

        )
        ),
        ('', (
            ('docente', 'Docente'),

        )
        ),
        ('', (
            ('estudiante', 'Estudiante'),

        )
        ),
        ('', (
            ('docente, estudiante', 'Docente, Estudiante'),

        )
        ),
        ('', (
            ('administrativo, docente', 'Administrativo, Docente'),

        )
        ),
        ('', (
            ('administrativo, docente, estudiante',
             'Administrativo, Docente, Estudiante'),

        )
        ),
        ('', (
            ('publico', 'Público'),

        )
        ),
    )
    id_servicio = models.CharField(max_length=2, primary_key=True) 
    conexion = models.ForeignKey(Conexion, on_delete=models.PROTECT)
    rol = models.CharField(max_length=50, choices=Rol)
    nombre = models.CharField(max_length=50)
    sql = models.TextField(max_length=500)
    descripcion = models.TextField(max_length=300)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('listar-servicios')

# Atributos de directorio telefónico
class Directorio(models.Model):
    dependencia = models.CharField(max_length=100)
    extension = models.CharField(max_length=50, blank=True)
    linea_directa = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.dependencia
    
    def get_absolute_url(self):
        return reverse('listar-directorios')

# Atributos de georreferenciación
class Localizacion(models.Model):
    descripcion = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    latitud = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
    
    def get_absolute_url(self):
        return reverse('listar-localizaciones')

# Atributos de artículos extravíados
class Articulo(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()
    foto = models.ImageField(upload_to='fotos_articulo/')

    def __str__(self):
        return self.descripcion
    
    def get_absolute_url(self):
        return reverse('listar-articulos')


@receiver(post_delete, sender=Articulo)
def articulo_delete(sender, instance, **kwargs):
    instance.foto.delete(False)

# Atributos de parametrización
class Parametrizacion(models.Model):

    Estado = (

        ('', (
            ('activo', 'Activo'),

        )
        ),
        ('', (
            ('inactivo', 'Inactivo'),

        )
        ),
    )

    nombre = models.CharField(max_length=200)
    lema = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='fotos_param')
    mision = models.TextField(max_length=500)
    vision = models.TextField(max_length=500)
    informacion = models.CharField(max_length=200)
    estado_directorio = models.CharField(max_length=50, choices=Estado)
    estado_articulo = models.CharField(max_length=50, choices=Estado)
    estado_localizacion = models.CharField(max_length=50, choices=Estado)
    hoja_de_vida = models.CharField(max_length=50, choices=Estado)
    oferta_academica = models.CharField(max_length=50, choices=Estado)
    nota_semestre = models.CharField(max_length=50, choices=Estado)
    informacion_materia = models.CharField(max_length=50, choices=Estado)
    lista_estudiantes = models.CharField(max_length=50, choices=Estado)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('listar-parametrizaciones')