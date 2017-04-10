from django.contrib.postgres.fields import JSONField
from django.db import models


class Appointment(models.Model):
    dates = JSONField()
    times = JSONField()


class User(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    e_mail = models.EmailField(max_length=255, null=False, blank=False)
    appointments = models.ManyToManyField(Appointment)
