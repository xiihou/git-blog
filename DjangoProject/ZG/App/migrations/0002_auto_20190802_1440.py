# Generated by Django 2.1.7 on 2019-08-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='douyin_info',
            name='d_account',
            field=models.CharField(max_length=48, unique=True),
        ),
        migrations.AlterField(
            model_name='douyin_info',
            name='user_id',
            field=models.IntegerField(unique=True),
        ),
    ]
