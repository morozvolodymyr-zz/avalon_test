from django.contrib.auth.models import AbstractUser
from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)


class RegisteredUser(AbstractUser):
    appointments = models.ManyToManyField(Appointment, blank=True)


class UnregisteredUser(models.Model):
    name = models.CharField(max_length=255)
    e_mail = models.EmailField(max_length=255)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)


class Date(models.Model):
    date = models.CharField(max_length=255, null=False, blank=False)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)


class Time(models.Model):
    time = models.CharField(max_length=255, null=False, blank=False)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
