from django.test import TestCase
from .models import Hotel

class HotelModelTest(TestCase):
    def test_creacion_hotel(self):
        hotel = Hotel.objects.create(
            nombre='Hotel de Prueba',
            ruc='1234567890'
        )
        self.assertEqual(str(hotel), 'Hotel de Prueba')
