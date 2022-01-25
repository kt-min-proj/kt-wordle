from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class User(models.Model):
    CLASS_CHOICES = (
		(0, '수도권1반'), (1, '수도권2반'), (2, '수도권3반'), (3, '수도권3반'), (4, '수도권3반'),
        (5, '강원권1반'), (6, '충남/충북권1반'), (7, '대구/경북권1반'), (8, '전남/전북권1반'), (9, '부산/경남권1반')
    )
    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(max_length=50, db_column='password')
    user_name = models.CharField(max_length=50, db_column='name')
    user_class = models.SmallIntegerField(choices=CLASS_CHOICES, db_column='class')

    class Meta:
        db_table = 'user'
        # managed = False