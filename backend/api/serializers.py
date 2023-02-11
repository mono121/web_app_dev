from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

# #トークンを発行するためのクラス
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)
#         return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # passwordはGETでアクセス禁止で必須。
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        # passwordのハッシュ化
        user = User.objects.create_user(**validated_data)
        # Token.objects.create(user=user)
        return user


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    created_at = serializers.DateTimeField(
        format="%Y-%m-%H:%M", read_only=True)
    updated_at = serializers.DateTimeField(
        format="%Y-%m-%H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'created_at', 'updated_at']
