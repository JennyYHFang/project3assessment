from django.db import models
from django.urls import reverse

# Create your models here.

class Wishitem(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

