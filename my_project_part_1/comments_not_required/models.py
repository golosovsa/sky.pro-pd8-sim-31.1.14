from django.db import models


class Calendar(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    comment = models.CharField(max_length=1000)
