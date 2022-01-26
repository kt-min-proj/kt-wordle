from django.db import models

from member.models import WordleUser


class WordleAnswers(models.Model):
    objects = None  # NOTE IDE error

    date = models.DateTimeField()
    answer = models.CharField(max_length=20)

    class Meta:
        db_table = "wordle_answer"


class WordleDayRanks(models.Model):
    objects = None

    count = models.IntegerField()
    create_at = models.DateTimeField()
    user = models.ForeignKey(WordleUser, on_delete=models.CASCADE)
    # NOTE 한개안에 두개의 fk를 사용시 오류발생
    # name = models.ForeignKey(WordleUser, on_delete=models.CASCADE)
    user_rank = models.IntegerField(null=True)

    class Meta:
        db_table = "wordle_dayrank"


class WordleRanks(models.Model):
    user = models.ForeignKey(WordleUser, on_delete=models.CASCADE)
    user_rank = models.IntegerField(null=True)
    date = models.DateField()

    class Meta:
        db_table = "wordle_rank"
