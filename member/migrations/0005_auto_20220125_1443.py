# Generated by Django 3.2.5 on 2022-01-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20220125_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordleuser',
            name='user_role',
            field=models.SmallIntegerField(choices=[('수도권1반', '수도권1반'), ('수도권2반', '수도권2반'), ('수도권3반', '수도권3반'), ('수도권4반', '수도권4반'), ('수도권5반', '수도권5반'), ('강원권1반', '강원권1반'), ('충남/충북권1반', '충남/충북권1반'), ('대구/경북권1반', '대구/경북권1반'), ('전남/전북권1반', '전남/전북권1반'), ('부산/경남권1반', '부산/경남권1반')], db_column='role', default=0),
        ),
        migrations.AlterField(
            model_name='wordleuser',
            name='user_class',
            field=models.CharField(choices=[('수도권1반', '수도권1반'), ('수도권2반', '수도권2반'), ('수도권3반', '수도권3반'), ('수도권4반', '수도권4반'), ('수도권5반', '수도권5반'), ('강원권1반', '강원권1반'), ('충남/충북권1반', '충남/충북권1반'), ('대구/경북권1반', '대구/경북권1반'), ('전남/전북권1반', '전남/전북권1반'), ('부산/경남권1반', '부산/경남권1반')], db_column='class', max_length=10),
        ),
    ]
