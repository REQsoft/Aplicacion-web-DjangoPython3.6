# Generated by Django 2.0.5 on 2018-05-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_auto_20180519_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sql',
            name='id_servicio',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
