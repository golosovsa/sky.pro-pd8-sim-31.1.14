from django.contrib.auth.models import User
from django.db import models


# TODO добавьте необходимый код в данный модуль
class Code(models.Model):
    code = models.CharField(max_length=4)


class Vacation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    code = models.CharField(max_length=4)
