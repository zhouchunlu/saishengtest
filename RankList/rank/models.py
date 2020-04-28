from django.db import models

# Create your models here.


class RankModel(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    client = models.CharField(verbose_name='客户端', max_length=64)
    score = models.IntegerField(verbose_name='分数', db_index=True)

