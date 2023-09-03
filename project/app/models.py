
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)
    followers = models.CharField(max_length=10)
    location = models.CharField(max_length=100, null=True, blank=True)