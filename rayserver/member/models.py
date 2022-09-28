from django.db import models


class Member(models.Model):
    member_id = models.CharField(db_column='member_id',max_length=50)
    passwd = models.CharField(db_column='passwd', max_length=50)
    name = models.CharField(db_column='name', max_length=50)
    email = models.CharField(db_column='email', max_length=50, blank=True)
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='y')
    reg_date = models.DateTimeField(db_column='reg_date', auto_now_add=True)
    update_date = models.DateTimeField(db_column='update_date', auto_now_add=True)

    class Meta:
#        managed = False
        db_table = 'member'

    def __str__(self):
        return '이름 : ' + self.name + ", 이메일 : " + self.email


class Members(models.Model):
    mem_id = models.CharField(verbose_name="회원 아이디", max_length=20, primary_key=True, null=False, default=False)
    mem_pw = models.TextField(verbose_name="회원 비밀번호", null=False)
    mem_name = models.CharField(verbose_name="회원 이름", max_length=30, null=False, default=False)
    mem_birth = models.DateField(verbose_name="회원 생년월일", null=False)
    mem_gender = models.CharField(verbose_name="회원 성별", max_length = 1, null=False)
    mem_joindate = models.DateField(verbose_name="회원 가입일자", auto_now_add=True)
    mem_type = models.CharField(verbose_name="회원 유형", max_length=1, null=False)

    class Meta:
        db_table = 't_member'
        verbose_name = '회원 테이블'

    def __str__(self):
        return '이름:' + self.mem_name + ", 성별: "+self.mem_gender




