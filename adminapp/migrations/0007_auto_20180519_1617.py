# Generated by Django 2.0.5 on 2018-05-19 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_auto_20180519_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sql',
            name='id',
        ),
        migrations.AddField(
            model_name='sql',
            name='id_servicio',
            field=models.CharField(default='', max_length=2, primary_key=True, serialize=False),
        ),
    ]
