# Generated by Django 4.1.1 on 2022-09-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnTable',
            fields=[
                ('column_seq', models.AutoField(primary_key=True, serialize=False, verbose_name='컬럼 순번')),
                ('column_title', models.CharField(max_length=400, verbose_name='컬럼 제목')),
                ('column_content', models.TextField(verbose_name='컬럼 내용')),
                ('column_img', models.ImageField(upload_to='', verbose_name='컬럼 이미지')),
                ('column_link', models.CharField(max_length=400, verbose_name='컬럼 출처')),
                ('column_date', models.DateField(auto_now_add=True, verbose_name='컬럼 날짜')),
            ],
            options={
                'verbose_name': '컬럼정보 테이블',
                'db_table': 't_column2',
            },
        ),
        migrations.CreateModel(
            name='FoodTable',
            fields=[
                ('food_seq', models.AutoField(primary_key=True, serialize=False, verbose_name='음식정보 순번')),
                ('food_info', models.TextField(verbose_name='음식 정보')),
                ('food_img', models.ImageField(upload_to='', verbose_name='음식 이미지')),
            ],
            options={
                'verbose_name': '음식정보 테이블',
                'db_table': 'q_food',
            },
        ),
        migrations.CreateModel(
            name='TrainingTable',
            fields=[
                ('train_seq', models.AutoField(primary_key=True, serialize=False, verbose_name='운동정보 순번')),
                ('train_info', models.TextField(verbose_name='운동 정보')),
                ('train_img', models.ImageField(upload_to='', verbose_name='운동 이미지')),
            ],
            options={
                'verbose_name': '운동정보 테이블',
                'db_table': 't_train2',
            },
        ),
    ]
