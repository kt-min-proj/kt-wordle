from django.db import models

# Create your models here.
class wordle_answers(models.Model):
    date = models.DateField(primary_key=True)
    answer = models.CharField(max_length=20)

    class Meta:
        db_table ='wordle_answer'


class wordle_users(models.Model):
    user_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    dclass = models.CharField(max_length=50)

    class Meta:
        db_table = 'wordle_user'


class wordle_dayRanks(models.Model):
    count = models.IntegerField()
    create_at = models.DateTimeField()
    user = models.ForeignKey(wordle_users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wordle_dayRank'


class wordle_ranks(models.Model):
    user = models.ForeignKey(wordle_users, on_delete=models.CASCADE)
    user_rank = models.IntegerField()
    # 이 부분은 데이트 필드만 둬도 괜찮을 것 같다.
    date = models.DateField()

    class Meta:
        db_table = 'wordle_rank'