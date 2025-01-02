from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Barber, Client, Service, Appointment, Payment

class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'


class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

# User Registration View
class UserRegisterView(FormView):
    template_name = 'app/Login/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

# User Login View
class UserLoginView(LoginView):
    template_name = 'app/Login/login.html'
    success_url = reverse_lazy('Barber')

# User Logout View
class UserLogoutView(LogoutView):
    template_name = 'app/Login/logout.html'

class AdminView(TemplateView):
    template_name = 'app/Admin/Admin.html'


class BarberListView(ListView):
    model = Barber
    context_object_name = 'barber'
    template_name = 'app/barber_list.html'


class BarberDetailView(DetailView):
    model = Barber
    context_object_name = 'barber'
    template_name = 'app/barber_detail.html'


class BarberCreateView(CreateView):
    model = Barber
    fields = ['user', 'name', 'experience_years', 'specialty', 'rating', 'available']
    template_name = 'app/barber_create.html'


class BarberUpdateView(UpdateView):
    model = Barber
    fields = ['user', 'name', 'experience_years', 'specialty', 'rating', 'available']
    template_name = 'app/barber_update.html'


class BarberDeleteView(DeleteView):
    model = Barber
    template_name = 'app/barber_delete.html'
    success_url = reverse_lazy('Barber')


class ClientListView(ListView):
    model = Client
    context_object_name = 'client'
    template_name = 'app/client_list.html'


class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'
    template_name = 'app/client_detail.html'


class ClientCreateView(CreateView):
    model = Client
    fields = ['firstname', 'lastname', 'phone', 'address']
    template_name = 'app/client_create.html'


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['firstname', 'lastname', 'phone', 'address']
    template_name = 'app/client_update.html'


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'app/client_delete.html'
    success_url = reverse_lazy('client')


class ServiceListView(ListView):
    model = Service
    context_object_name = 'service'
    template_name = 'app/service_list.html'


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'app/service_detail.html'


class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'description', 'duration', 'price']
    template_name = 'app/service_create.html'


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['name', 'description', 'duration', 'price']
    template_name = 'app/service_update.html'

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'app/service_delete.html'
    success_url = reverse_lazy('service')

class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/appointment_list.html'

class AppointmentDetailView(DetailView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/appointment_detail.html'


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['barber', 'client', 'service', 'date', 'time',  'updated_at', 'status']
    template_name = 'app/appointment_create.html'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['barber', 'client', 'service', 'date', 'time', 'updated_at', 'status']
    exclude = ['created_at']
    template_name = 'app/appointment_update.html'

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app/appointment_delete.html'
    success_url = reverse_lazy('appointment')

class PaymentListView(ListView):
    model = Payment
    context_object_name = 'payment'
    template_name = 'app/payment_list.html'


class PaymentDetailView(DetailView):
    model = Payment
    context_object_name = 'payment'
    template_name = 'app/payment_detail.html'

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['appointment', 'amount', 'method', 'payment_date', ]
    template_name = 'app/payment_create.html'

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['appointment', 'amount', 'method', 'payment_date', ]
    template_name = 'app/payment_update.html'

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'app/payment_delete.html'
    success_url = reverse_lazy('payment')












