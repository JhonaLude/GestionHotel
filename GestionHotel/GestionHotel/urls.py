from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from GestionHotel import views

urlpatterns = [
    # Redirige la raíz al login
    path('', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        next_page='/hoteles/',
    ), name='login'),

    # Admin de Django
    path('admin/', admin.site.urls),

    # Ruta de login y logout 
    path('accounts/', include('django.contrib.auth.urls')),  
    
    # Rutas para Hotel
    path('hoteles/', views.hotel_list, name='hotel_list'),
    path('hoteles/create/', views.hotel_create, name='hotel_create'),
    path('hoteles/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('hoteles/<int:pk>/update/', views.hotel_update, name='hotel_update'),
    path('hoteles/<int:pk>/delete/', views.hotel_delete, name='hotel_delete'),
    
    # Rutas para Habitación
    path('habitaciones/', views.habitacion_list, name='habitacion_list'),
    path('habitaciones/create/', views.habitacion_create, name='habitacion_create'),
    path('habitaciones/<int:pk>/', views.habitacion_detail, name='habitacion_detail'),
    path('habitaciones/<int:pk>/update/', views.habitacion_update, name='habitacion_update'),
    path('habitaciones/<int:pk>/delete/', views.habitacion_delete, name='habitacion_delete'),
    
    # Rutas para Reservación
    path('reservaciones/', views.reservacion_list, name='reservacion_list'),
    path('reservaciones/create/', views.reservacion_create, name='reservacion_create'),
    path('reservaciones/<int:pk>/', views.reservacion_detail, name='reservacion_detail'),
    path('reservaciones/<int:pk>/update/', views.reservacion_update, name='reservacion_update'),
    path('reservaciones/<int:pk>/delete/', views.reservacion_delete, name='reservacion_delete'),
    
    # Rutas para Factura
    path('facturas/', views.factura_list, name='factura_list'),
    path('facturas/create/', views.factura_create, name='factura_create'),
    path('facturas/<int:pk>/', views.factura_detail, name='factura_detail'),
    path('facturas/<int:pk>/update/', views.factura_update, name='factura_update'),
    path('facturas/<int:pk>/delete/', views.factura_delete, name='factura_delete'),
]