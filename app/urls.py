from django.urls import path
from .views import (HomePageView, AboutPageView, ContactPageView, BarberListView,
                    BarberDetailView, BarberCreateView, BarberUpdateView, BarberDeleteView,
                    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView,
                    ClientDeleteView, ServiceListView, ServiceDetailView, ServiceCreateView,
                    ServiceUpdateView, ServiceDeleteView, AppointmentListView, AppointmentDetailView,
                    AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView, PaymentListView,
                    PaymentDetailView, PaymentCreateView, PaymentUpdateView, PaymentDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('barber/', BarberListView.as_view(), name='Barber'),
    path('barber/<int:pk>', BarberDetailView.as_view(), name='barber_detail'),
    path('barber/create', BarberCreateView.as_view(), name='barber_create'),
    path('barber/<int:pk>/edit', BarberUpdateView.as_view(), name='barber_update'),
    path('barber/<int:pk>/delete', BarberDeleteView.as_view(), name='barber_delete'),

    path('client/', ClientListView.as_view(), name='client'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/edit', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete', ClientDeleteView.as_view(), name='client_delete'),

    path('service/', ServiceListView.as_view(), name='service'),
    path('service/<int:pk>', ServiceDetailView.as_view(), name='service_detail'),
    path('service/create', ServiceCreateView.as_view(), name='service_create'),
    path('service/<int:pk>/edit', ServiceUpdateView.as_view(), name='service_update'),
    path('service/<int:pk>/delete', ServiceDeleteView.as_view(), name='service_delete'),

    
    path('appointment/', AppointmentListView.as_view(), name='appointment'),
    path('appointment/<int:pk>', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment/create', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/edit', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/<int:pk>/delete', AppointmentDeleteView.as_view(), name='appointment_delete'),

    path('payment/', PaymentListView.as_view(), name='service'),
    path('payment/<int:pk>', PaymentDetailView.as_view(), name='payment_detail'),
    path('paymentyment/create', PaymentCreateView.as_view(), name='payment_create'),
    path('payment/<int:pk>/edit', PaymentUpdateView.as_view(), name='payment_update'),
    path('payment/<int:pk>/delete', PaymentDeleteView.as_view(), name='payment_delete'),


]