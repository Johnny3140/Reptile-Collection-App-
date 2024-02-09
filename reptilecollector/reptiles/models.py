from django.db import models
from django.apps import apps

class Reptile(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Feeding(models.Model):
    reptile = models.ForeignKey(Reptile, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=50)
    notes = models.TextField()