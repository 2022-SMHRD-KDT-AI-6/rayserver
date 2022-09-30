from django.db import models
from member.models import Members

# Create your models here.
class FoodTable(models.Model):
    food_seq = models.AutoField(verbose_name="음식정보 순번", primary_key=True)
    food_info = models.TextField(verbose_name="음식 정보", null=False)
    food_img = models.ImageField(verbose_name="음식 이미지")
    class Meta:
        db_table = 'q_food'
        verbose_name = '음식정보 테이블'
    def __str__(self):
        return str(self.food_img)  # 수정
    def summary(self):
        return self.body[:100]




