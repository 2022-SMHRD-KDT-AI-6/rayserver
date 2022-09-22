from django.db import models
from member.models import Members

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="%Y/%m/%d", null=False)

    class Meta:
        db_table = 'imagetest1'
        verbose_name = '이미지테스트1'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

class Sale(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    




class Test(models.Model):
    mem_seq = models.AutoField(primary_key=True)
    exam_img = models.ImageField(verbose_name="검사 이미지",  null=False)
    exam_date = models.DateTimeField(verbose_name="검사 날짜", auto_now_add=True)
    exam_result = models.TextField(verbose_name="검사 결과",  null=False)
    mem_id = models.ForeignKey(Members, verbose_name="회원 아이디", on_delete=models.CASCADE, null=False)
    class Meta:
        db_table = 't_exam2'
        verbose_name = '검사 테이블2'

class Test1(models.Model):    
    author = models.ForeignKey(Members, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(
            blank=True, null=True)
    upload_file = models.ImageField(    #유효성 검사를 위해서 ImageField를 사용
        blank=True,#해당 속성이 비어도 되는지 유무
        null=True,#null이 들어가도 되는지 유무
        upload_to="image"#경로 설정 (입력 안하면 uploads에 바로 올라가짐)
        )
    class Meta:
        db_table = 'imgtest2'
        verbose_name = '이미지테스트2'

class Test2(models.Model):
    mem_seq = models.AutoField(primary_key=True)
    exam_img = models.ImageField(verbose_name="검사 이미지",  null=False)
    exam_date = models.DateTimeField(verbose_name="검사 날짜", auto_now_add=True)
    exam_result = models.TextField(verbose_name="검사 결과",  null=False)
    mem_id = models.CharField(verbose_name="회원 아이디", max_length=200)
    class Meta:
        db_table = 'test2'
        verbose_name = 'test2'

