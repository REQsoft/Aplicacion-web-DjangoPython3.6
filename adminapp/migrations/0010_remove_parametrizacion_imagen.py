# Generated by Django 2.0.6 on 2018-07-09 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_auto_20180709_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parametrizacion',
            name='imagen',
        ),
    ]
