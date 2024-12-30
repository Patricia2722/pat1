from django.contrib import admin
from .models import Barber, Client, Service, Appointment, Payment

admin.site.register(Barber)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Payment)
