# Generated by Django 4.2.11 on 2025-02-01 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_habitacion', models.IntegerField()),
                ('tipo', models.CharField(choices=[('suite', 'Suite'), ('doble', 'Doble'), ('individuales', 'Individuales')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HabitacionReservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.habitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('habitaciones', models.ManyToManyField(through='GestionHotel.HabitacionReservacion', to='GestionHotel.habitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('spa', 'Spa'), ('comida', 'Comida'), ('transporte', 'Transporte'), ('estacionamiento', 'Estacionamiento')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ReservacionAgencia',
            fields=[
                ('reservacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='GestionHotel.reservacion')),
                ('nombre_agencia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReservacionParticular',
            fields=[
                ('reservacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='GestionHotel.reservacion')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=20, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('anio_construccion', models.PositiveIntegerField(blank=True, null=True)),
                ('categoria', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='GestionHotel.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='habitacionreservacion',
            name='reservacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.reservacion'),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitaciones', to='GestionHotel.hotel'),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_factura', models.DateField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('iva', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('metodo_pago', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')], max_length=20)),
                ('reservacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.reservacion')),
            ],
        ),
        migrations.CreateModel(
            name='HabitacionServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fin', models.TimeField(blank=True, null=True)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.habitacion')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.servicio')),
            ],
            options={
                'unique_together': {('habitacion', 'servicio')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='habitacionreservacion',
            unique_together={('habitacion', 'reservacion')},
        ),
    ]
