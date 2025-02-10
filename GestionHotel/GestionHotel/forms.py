from django import forms
from .models import Hotel, Habitacion, Reservacion, Factura

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = '__all__'

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
