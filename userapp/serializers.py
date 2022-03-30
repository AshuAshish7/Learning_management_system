from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullName', 'password', 'userName', 'dob', 'userType']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'userName', 'role',]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullName', 'userName', 'unique_id', 'role']