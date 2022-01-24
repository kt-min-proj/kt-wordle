from django.db import models

# Create your models here.


class Calendar(models.Model):
    date = models.CharField(max_length=12)
