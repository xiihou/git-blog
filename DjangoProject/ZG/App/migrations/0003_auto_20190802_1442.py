# Generated by Django 2.1.7 on 2019-08-02 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20190802_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='douyin_info',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
