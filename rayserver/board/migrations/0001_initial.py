# Generated by Django 4.1.1 on 2022-09-23 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('mem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.members')),
            ],
            options={
                'verbose_name': '테스트33',
                'db_table': 'test33',
            },
        ),
    ]
