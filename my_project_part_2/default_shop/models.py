from django.db import models


class Store(models.Model):
    store_id = models.CharField(max_length=100, primary_key=True)
    store_info = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    is_photo_needed = models.BooleanField(default=False)

    def __str__(self):
        return f"{{Store({self.pk}-{self.store_id})}}"
