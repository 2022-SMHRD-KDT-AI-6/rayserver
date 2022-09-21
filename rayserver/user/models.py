from tabnanny import verbose
from django.db import models

# Create your models here.
class LoginUser(models.Model):
    user_id = models.CharField(max_length=20, unique=True, null=False, default=False)
    user_pw = models.CharField(max_length=255, null=False, default=False)
    birth_day = models.DateField(verbose_name="생년월일", null=True)
    gender = models.CharField(verbose_name="성별", max_length=6, null=False, default='male')
    email = models.CharField(verbose_name="이메일 주소", max_length=255, null=False, default='')
    name = models.CharField(verbose_name="이름", max_length=20, null=True)
    age = models.IntegerField(verbose_name="나이", default=20)
    class Meta:
        db_table = 'login_user'
        verbose_name = '로그인 테스트 테이블'

# 아이디, 패스워드, 이름, 생년월일, 성별, 가입날짜, 회원유형

class JoinTable(models.Model):
    mem_id = models.CharField(verbose_name="회원 아이디", max_length=20, primary_key=True, null=False, default=False)
    mem_pw = models.TextField(verbose_name="회원 비밀번호", null=False)
    mem_name = models.CharField(verbose_name="회원 이름", max_length=30, null=False, default=False)
    mem_birth = models.DateField(verbose_name="회원 생년월일", null=False)
    mem_gender = models.CharField(verbose_name="회원 성별", max_length = 1, null=False)
    mem_joindate = models.DateField(verbose_name="회원 가입일자", null=False, auto_now_add=True)
    mem_type = models.CharField(verbose_name="회원 유형", max_length=1, null=False)
    class Meta:
        db_table = 't_member22'
        verbose_name = '회원 테이블'

    def __str__(self):
        return '이름:' + self.mem_name + ", 성별: "+self.mem_gender




