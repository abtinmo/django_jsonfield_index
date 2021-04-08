from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=20)
    attributes = models.JSONField()
    create_date = models.DateTimeField(default=timezone.now)
