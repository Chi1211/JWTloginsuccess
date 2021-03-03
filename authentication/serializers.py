from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate
import jwt
from datetime import datetime, timedelta
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, style={"input_type": "password"})
    password2=serializers.CharField(write_only=True, style={"input_name": "password"})

    class Meta:
        model= User
        fields=['username', 'email', 'password','password2']

        extra_kwargs={"password":{"write_oly":True}}

    def create(self, validate_data):
        username=validate_data["username"]
        email=validate_data["email"]
        password=validate_data["password"]
        password2=validate_data["password2"]

        if User.objects.filter(username=username):
            raise serializers.ValidationError({"username":"usename already exists"})
        if User.objects.filter(email=email):
            raise serializers.ValidationError({"email": "email already exists"})
        if " " in password:
            raise serializers.ValidationError({"password": "password cannot contain spaces"})
        if password !=password2:
            raise serializers.ValidationError({"password": "password do not match"})

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(write_only=True, style={"input_type": "password"}, max_length=64)
    class Meta:
        model=User
        fields=['username','password']

    def validate(self, validate_data):
        username=validate_data.get('username', None)
        password=validate_data.get('password', None)

        user=authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError({"user":"User with given email and password does not exists"})
        else:
        
            auth_token=jwt.encode({
                'id': user.id,
                'exp': datetime.utcnow() + timedelta(minutes=5)
                }, settings.SECRET_KEY, algorithm="HS256")
            
            validate_data['user']=user
            validate_data['token']=auth_token
            return validate_data
    