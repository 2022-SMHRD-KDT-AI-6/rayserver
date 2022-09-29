# Generated by Django 4.1.1 on 2022-09-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
    ]
