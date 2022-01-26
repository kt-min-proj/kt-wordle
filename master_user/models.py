from django.db import models

from member.models import WordleUser


class WordleAnswers(models.Model):
    objects = None  # NOTE IDE error

    date = models.DateField(primary_key=True)
    answer = models.CharField(max_length=20)

    class Meta:
        db_table = "wordle_answer"


class WordleDayRanks(models.Model):
    objects = None

    count = models.IntegerField()
    create_at = models.DateTimeField()
    user = models.ForeignKey(WordleUser, on_delete=models.CASCADE)
    user_rank = models.IntegerField()

    class Meta:
        db_table = "wordle_dayrank"


class WordleRanks(models.Model):
    user = models.ForeignKey(WordleUser, on_delete=models.CASCADE)
    user_rank = models.IntegerField()
    # 이 부분은 데이트 필드만 둬도 괜찮을 것 같다.
    date = models.DateField()

    class Meta:
        db_table = "wordle_rank"
