from django.db import models
from django import forms

from .validators import password_validator

# Create your models here.


class WordleUser(models.Model):
    objects = None
    CLASS_CHOICES = (
        ("수도권1반", "수도권1반"),
        ("수도권2반", "수도권2반"),
        ("수도권3반", "수도권3반"),
        ("수도권4반", "수도권4반"),
        ("수도권5반", "수도권5반"),
        ("강원권1반", "강원권1반"),
        ("충남/충북권1반", "충남/충북권1반"),
        ("대구/경북권1반", "대구/경북권1반"),
        ("전남/전북권1반", "전남/전북권1반"),
        ("부산/경남권1반", "부산/경남권1반"),
    )
    ROLE_CHOICES = (
        (0, "일반유저"),
        (1, "관리유저"),
    )
    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(
        max_length=50, validators=[password_validator], db_column="password"
    )
    user_name = models.CharField(max_length=50, db_column="name")
    user_class = models.CharField(
        max_length=10, choices=CLASS_CHOICES, db_column="class"
    )
    user_role = models.SmallIntegerField(
        choices=CLASS_CHOICES, default=0, db_column="role"
    )

    class Meta:
        db_table = "wordle_user"
        # managed = False
