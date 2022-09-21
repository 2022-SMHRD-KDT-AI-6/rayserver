from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="%Y/%m/%d", null=False)

    class Meta:
        db_table = 'imagetest1'
        verbose_name = '이미지테스트1'

