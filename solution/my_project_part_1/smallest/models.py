from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class SmallPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=20, unique=True)
    text = models.CharField(max_length=1000, validators=[MinLengthValidator(5)])
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
