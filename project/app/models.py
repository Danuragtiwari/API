
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField()
    #
