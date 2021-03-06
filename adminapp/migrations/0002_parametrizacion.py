# Generated by Django 2.0.5 on 2018-05-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametrizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('lema', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='fotos_param')),
                ('mision', models.TextField(max_length=500)),
                ('vision', models.TextField(max_length=500)),
                ('informacion', models.CharField(max_length=200)),
                ('estado_directorio', models.CharField(choices=[('', (('activo', 'Activo'),)), ('', (('inactivo', 'Inactivo'),))], max_length=50)),
                ('estado_articulo', models.CharField(choices=[('', (('activo', 'Activo'),)), ('', (('inactivo', 'Inactivo'),))], max_length=50)),
                ('estado_localizacion', models.CharField(choices=[('', (('activo', 'Activo'),)), ('', (('inactivo', 'Inactivo'),))], max_length=50)),
                ('hoja_de_vida', models.CharField(choices=[('', (('activo', 'Activo'),)), ('', (('inactivo', 'Inactivo'),))], max_length=50)),
                ('oferta_academica', models.CharField(choices=[('', (('activo', 'Activo'),)), ('', (('inactivo', 'Inactivo'),))], max_length=50)),
                ('nota_semestre', models.CharField(choices=[('', (('activo', 'Activo'),)), ('', (('inactivo', 'Inactivo'),))], max_length=50)),
                ('informacion_materia', models.CharField(choices=[('', (('activo', 'Activo'),)), ('', (('inactivo', 'Inactivo'),))], max_length=50)),
                ('lista_estudiantes', models.CharField(choices=[('', (('activo', 'Activo'),)), ('', (('inactivo', 'Inactivo'),))], max_length=50)),
            ],
        ),
    ]
