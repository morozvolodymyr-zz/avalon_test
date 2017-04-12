from django.contrib.auth.models import AbstractUser
from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)


class RegisteredUser(AbstractUser):
    email = models.EmailField(max_length=255, null=False, blank=False)


class Date(models.Model):
    date = models.CharField(max_length=255, null=False, blank=False)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)


class Time(models.Model):
    time = models.CharField(max_length=255, null=False, blank=False)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)


class Registration(models.Model):
    name = models.CharField(max_length=255)
    e_mail = models.EmailField(max_length=255)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE, blank=True)
