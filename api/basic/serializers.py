from rest_framework import serializers

from basic.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        
class AdvancedUserSerializer(serializers.ModelSerializer):
    uid = UserSerializer(serializers.ModelSerializer, required=True)
    class Meta:
        model = AdvancedUser
        fields = ('uid',  'gender', 'age')
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pid', 'title')
        
class PostContentSerializer(serializers.ModelSerializer):
    pid = PostSerializer(serializers.ModelSerializer, required=True)
    uid = UserSerializer(serializers.ModelSerializer, required=True)
    class Meta:
        model = PostContent
        fields = ('pid', 'uid', 'content')
        
class SystemMesgSerializer(serializers.ModelSerializer):
    uid = UserSerializer(serializers.ModelSerializer, required=True)
    class Meta:
        model = SystemMesg
        fields = ('mid', 'uid', 'content')