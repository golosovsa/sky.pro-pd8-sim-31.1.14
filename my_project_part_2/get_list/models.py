from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=2, decimal_places=1)
