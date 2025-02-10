from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Habitacion, Reservacion, Factura
from .forms import HotelForm, HabitacionForm, ReservacionForm, FacturaForm
from django.contrib.auth.decorators import login_required

# ----- VISTAS PARA HOTEL -----

@login_required
def hotel_list(request):
    hoteles = Hotel.objects.all()
    return render(request, 'GestionHotel/hotel_list.html', {'hoteles': hoteles})

@login_required
def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'GestionHotel/hotel_detail.html', {'hotel': hotel})

@login_required
def hotel_create(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
    else:
        form = HotelForm()
    return render(request, 'GestionHotel/hotel_form.html', {'form': form})

@login_required
def hotel_update(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel_detail', pk=pk)
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'GestionHotel/hotel_form.html', {'form': form})

@login_required
def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotel_list')
    return render(request, 'GestionHotel/hotel_confirm_delete.html', {'hotel': hotel})

# ----- VISTAS PARA HABITACION -----

@login_required
def habitacion_list(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'GestionHotel/habitacion_list.html', {'habitaciones': habitaciones})

@login_required
def habitacion_detail(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    return render(request, 'GestionHotel/habitacion_detail.html', {'habitacion': habitacion})

@login_required
def habitacion_create(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('habitacion_list')
    else:
        form = HabitacionForm()
    return render(request, 'GestionHotel/habitacion_form.html', {'form': form})

@login_required
def habitacion_update(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect('habitacion_detail', pk=pk)
    else:
        form = HabitacionForm(instance=habitacion)
    return render(request, 'GestionHotel/habitacion_form.html', {'form': form})

@login_required
def habitacion_delete(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    if request.method == 'POST':
        habitacion.delete()
        return redirect('habitacion_list')
    return render(request, 'GestionHotel/habitacion_confirm_delete.html', {'habitacion': habitacion})

# ----- VISTAS PARA RESERVACION -----

@login_required
def reservacion_list(request):
    reservaciones = Reservacion.objects.all()
    return render(request, 'GestionHotel/reservacion_list.html', {'reservaciones': reservaciones})

@login_required
def reservacion_detail(request, pk):
    reservacion = get_object_or_404(Reservacion, pk=pk)
    return render(request, 'GestionHotel/reservacion_detail.html', {'reservacion': reservacion})

@login_required
def reservacion_create(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservacion_list')
    else:
        form = ReservacionForm()
    return render(request, 'GestionHotel/reservacion_form.html', {'form': form})

@login_required
def reservacion_update(request, pk):
    reservacion = get_object_or_404(Reservacion, pk=pk)
    if request.method == 'POST':
        form = ReservacionForm(request.POST, instance=reservacion)
        if form.is_valid():
            form.save()
            return redirect('reservacion_detail', pk=pk)
    else:
        form = ReservacionForm(instance=reservacion)
    return render(request, 'GestionHotel/reservacion_form.html', {'form': form})

@login_required
def reservacion_delete(request, pk):
    reservacion = get_object_or_404(Reservacion, pk=pk)
    if request.method == 'POST':
        reservacion.delete()
        return redirect('reservacion_list')
    return render(request, 'GestionHotel/reservacion_confirm_delete.html', {'reservacion': reservacion})

# ----- VISTAS PARA FACTURA -----

@login_required
def factura_list(request):
    facturas = Factura.objects.all()
    return render(request, 'GestionHotel/factura_list.html', {'facturas': facturas})

@login_required
def factura_detail(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    return render(request, 'GestionHotel/factura_detail.html', {'factura': factura})

@login_required
def factura_create(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('factura_list')
    else:
        form = FacturaForm()
    return render(request, 'GestionHotel/factura_form.html', {'form': form})

@login_required
def factura_update(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('factura_detail', pk=pk)
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'GestionHotel/factura_form.html', {'form': form})

@login_required
def factura_delete(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        factura.delete()
        return redirect('factura_list')
    return render(request, 'GestionHotel/factura_confirm_delete.html', {'factura': factura})