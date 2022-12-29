from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework.validators import UniqueValidator


# TODO добавьте необходимый код в данный модуль
class Code(models.Model):
    code = models.CharField(max_length=4)


def is_code_exists(code: str):
    if not Code.objects.filter(code=code).exists():
        raise ValidationError(f"{code} is not exists in Code")


class Vacation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    code = models.CharField(max_length=4, validators=[is_code_exists])
