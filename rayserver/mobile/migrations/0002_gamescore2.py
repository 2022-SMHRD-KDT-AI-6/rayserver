# Generated by Django 4.1.1 on 2022-10-04 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameScore2',
            fields=[
                ('game_seq', models.AutoField(primary_key=True, serialize=False, verbose_name='게임 순번')),
                ('game_score1', models.CharField(db_column='최고 점수1', max_length=50, null=True)),
                ('game_score2', models.CharField(db_column='최고 점수2', max_length=50, null=True)),
                ('game_score3', models.CharField(db_column='최고 점수3', max_length=50, null=True)),
                ('game_score4', models.CharField(db_column='최고 점수4', max_length=50, null=True)),
                ('mem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.members', verbose_name='회원 아이디')),
            ],
            options={
                'verbose_name': '게임 테이블',
                'db_table': 't_game22',
            },
        ),
    ]