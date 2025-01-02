from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Barber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="barber_profile")
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    specialty = models.CharField(max_length=255, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("barber_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} - {self.specialty if self.specialty else 'General Barber'}"



class Client(models.Model):
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.firstname} "  f"{self.lastname}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(help_text="Duration of the service (e.g., 00:30:00 for 30 minutes)")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Appointment(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name="appointments")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], default='scheduled')
    notes = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("appointment_detail", kwargs={"pk": self.pk})


    def __str__(self):
        return f"Appointment for {self.client} with {self.barber} on {self.date} at {self.time}"

class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    method = models.CharField(max_length=20, choices=[
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('online', 'Online')
    ], default='card')
    payment_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("payment_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Payment of ${self.amount} for appointment on {self.appointment.date}"


    
