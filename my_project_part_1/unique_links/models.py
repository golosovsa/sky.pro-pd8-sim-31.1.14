from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


# TODO добавьте необходимый код в модель UniquePost
class UniquePost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=20, unique=True)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

