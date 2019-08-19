from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserInfo(AbstractUser):
    id = models.IntegerField(auto_created=True,primary_key=True)
    u_create_time = models.DateTimeField()
    u_invitation = models.CharField(max_length=24)
    u_be_invitation = models.CharField(max_length=24)
    u_status = models.CharField(max_length=4)


class DouYin_Info(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user_id = models.IntegerField()
    d_account =  models.CharField(max_length=48,unique=True)
    d_passwd = models.CharField(max_length=128)
    d_status = models.CharField(max_length=4)
    d_updata_time = models.DateTimeField(null=True)





