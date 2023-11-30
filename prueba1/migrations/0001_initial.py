# Generated by Django 4.2.7 on 2023-11-30 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_del_area', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Edad', models.PositiveIntegerField()),
                ('DUI', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Edad', models.PositiveIntegerField()),
                ('Area_DUI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba1.area')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_Venta', models.DateTimeField()),
                ('Monto', models.FloatField()),
                ('Clienteid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba1.cliente')),
                ('EmpleadoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba1.empleado')),
            ],
        ),
    ]
