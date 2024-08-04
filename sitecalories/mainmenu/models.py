from django.db import models

# Create your models here.


class Listofproducts(models.Model):
    name_product = models.CharField(max_length=20, blank=False)
    calories = models.FloatField(default=0)