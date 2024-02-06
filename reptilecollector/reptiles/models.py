from django.db import models
from django.apps import apps

class Reptile(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name