from django.db import models

# Create your models here.
class PlaceInfo(models.Model):
    category = models.CharField(verbose_name="구분", max_length=50)
    name = models.CharField(verbose_name="시설명", max_length=50)
    address = models.CharField(verbose_name="주소", max_length=300)
    tel = models.CharField(verbose_name="전화번호", max_length=50)

    def __str__(self):
        return self.category
    def summary(self):
        return self.body[:100]