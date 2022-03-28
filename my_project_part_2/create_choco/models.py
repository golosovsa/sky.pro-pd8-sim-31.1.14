from django.db import models


class Chocolate(models.Model):

    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=1)
    description = models.CharField(max_length=100)
