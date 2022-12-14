from unittest.util import _MAX_LENGTH
from django.db import models
from member.models import Members

# Create your models here.
class FoodTable3(models.Model):
    food_seq = models.AutoField(verbose_name="음식정보 순번", primary_key=True)
    food_title = models.CharField(verbose_name="음식 제목", max_length=400, null=False)
    food_info = models.TextField(verbose_name="음식 정보", null=False)
    food_img = models.ImageField(verbose_name="음식 이미지")
    class Meta:
        db_table = 't_food3'
        verbose_name = '음식정보 테이블'
    def __str__(self):
        return str(self.food_img)  # 수정
    def summary(self):
        return self.body[:100]

class TrainingTable3(models.Model):
    train_seq = models.AutoField(verbose_name="운동정보 순번", primary_key=True)
    train_title = models.CharField(verbose_name="운동 제목", max_length=400, null=False)
    train_info = models.TextField(verbose_name="운동 정보",  null=False)
    train_img = models.ImageField(verbose_name="운동 이미지")
    class Meta:
        db_table = 't_train3'
        verbose_name = '운동정보 테이블'
    def __str__(self):
        return str(self.train_seq)  # 수정
    def summary(self):
        return self.body[:100]



class ColumnTable(models.Model):
    column_seq = models.AutoField(verbose_name="컬럼 순번", primary_key=True)
    column_title = models.CharField(verbose_name="컬럼 제목", max_length=400, null=False)
    column_content = models.TextField(verbose_name="컬럼 내용", null=False)
    column_img = models.ImageField(verbose_name="컬럼 이미지")
    column_link = models.CharField(verbose_name="컬럼 출처", max_length=400)
    column_date = models.DateField(verbose_name="컬럼 날짜", auto_now_add=True)
    class Meta:
        db_table = 't_column4'
        verbose_name='컬럼정보 테이블'
    def __str__(self):
        return str(self.column_seq)  # 수정
    def summary(self):
        return self.body[:100]



