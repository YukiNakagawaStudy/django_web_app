from rest_framework import serializers
import logging
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', "username", "first_name", "last_name")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print ("Validated Data = ", validated_data)
        user = User.objects.create_user(email=validated_data['email'],
                                        password=validated_data['password'],
                                        username=validated_data['username'],
                                        first_name=validated_data["first_name"],
                                        last_name=validated_data["last_name"])
        return user


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)


class SignOutSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


def info(msg):
    logger = logging.getLogger('command')
    logger.info(msg)
