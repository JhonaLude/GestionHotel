from django.contrib import admin
from .models import (
    Categoria, Hotel, Habitacion, Servicio, HabitacionServicio,
    Reservacion, ReservacionParticular, ReservacionAgencia,
    HabitacionReservacion, Factura
)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ruc', 'direccion', 'telefono', 'anio_construccion', 'categoria']

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotel', 'numero_habitacion', 'tipo']

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo']

@admin.register(HabitacionServicio)
class HabitacionServicioAdmin(admin.ModelAdmin):
    list_display = ['habitacion', 'servicio', 'hora_inicio', 'hora_fin']

@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_persona', 'telefono', 'fecha_inicio', 'fecha_fin']

@admin.register(ReservacionParticular)
class ReservacionParticularAdmin(admin.ModelAdmin):
    list_display = ['reservacion']

@admin.register(ReservacionAgencia)
class ReservacionAgenciaAdmin(admin.ModelAdmin):
    list_display = ['reservacion', 'nombre_agencia']

@admin.register(HabitacionReservacion)
class HabitacionReservacionAdmin(admin.ModelAdmin):
    list_display = ['habitacion', 'reservacion']

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id', 'reservacion', 'fecha_factura', 'metodo_pago']
