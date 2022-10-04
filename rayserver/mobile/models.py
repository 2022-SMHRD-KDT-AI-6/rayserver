from django.db import models
from member.models import Members

class GameScore(models.Model):
    game_seq = models.AutoField(verbose_name="게임 순번",  primary_key=True)
    game_score1 = models.IntegerField(verbose_name="최고 점수1")
    game_score2 = models.IntegerField(verbose_name="최고 점수2")
    game_score3 = models.IntegerField(verbose_name="최고 점수3")
    game_score4 = models.IntegerField(verbose_name="최고 점수4")
    mem = models.ForeignKey(Members, verbose_name="회원 아이디", on_delete=models.CASCADE, null=False)
    class Meta:
        db_table = 't_game2'
        verbose_name = '게임 테이블'
    def __str__(self):
        return str(self.game_seq)
    def summary(self):
        return self.body[:100]

class GameScore2(models.Model):
    game_seq = models.AutoField(verbose_name="게임 순번",  primary_key=True)
    game_score1 = models.CharField(db_column='최고 점수1', max_length=50, null=True)
    game_score2 = models.CharField(db_column='최고 점수2', max_length=50, null=True)
    game_score3 = models.CharField(db_column='최고 점수3', max_length=50, null=True)
    game_score4 = models.CharField(db_column='최고 점수4', max_length=50, null=True)
    mem = models.ForeignKey(Members, verbose_name="회원 아이디", on_delete=models.CASCADE, null=False)
    class Meta:
        db_table = 't_game22'
        verbose_name = '게임 테이블'
    def __str__(self):
        return self.mem
    def summary(self):
        return self.body[:100]