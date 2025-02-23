from django.db import models

# Create your models here.
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()

class Emergency(models.Model):
    description = models.TextField()
    contact_number = models.CharField(max_length=15)

class Consultation(models.Model):
    name = models.CharField(max_length=100)
    query = models.TextField()

class MedicineOrder(models.Model):
    name = models.CharField(max_length=100)
    medicine_details = models.TextField()