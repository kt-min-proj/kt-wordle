from django.db import models


class Calendar(models.Model):
    objects = None
    date = models.DateField(primary_key='date')
    answer = models.CharField(max_length=20)

    class Meta:
        db_table = "wordle_answer"
