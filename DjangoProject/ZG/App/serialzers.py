from rest_framework import serializers
from .models import UserInfo,DouYin_Info


class UserInfoSerializer(serializers.Serializer):
    pass
#
# id = models.IntegerField(auto_created=True, primary_key=True)
# user_id = models.IntegerField()
# d_account =  models.CharField(max_length=48)
# d_passwd = models.CharField(max_length=128)
# d_status = models.CharField(max_length=4)

class DouYinInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    d_account = serializers.CharField(max_length=48)
    d_passwd = serializers.CharField(max_length=128)
    d_status = serializers.CharField(max_length=4)
