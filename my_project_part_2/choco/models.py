from django.db import models


class Chocolate(models.Model):
    name = models.CharField(max_length=20)
