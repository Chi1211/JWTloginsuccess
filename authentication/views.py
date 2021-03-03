from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework import status
# Create your views here.
class RegisterView(APIView):
    permission_classes=(AllowAny,)

    def post(self, request):
        serializers=RegisterSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        response={
            'user':serializers.data,
            'status_code':201
        }    
        return Response(response, status=201)

class LoginView(APIView):
    permission_classes=(AllowAny,)
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token=serializer.validated_data['token']
        login(request, user)           
        response={
            "username": user.username,
            "password":user.password,
            "token": token,
            "status_code" : status.HTTP_200_OK,
        }

        return Response(response, status=200)

class Logout(APIView):
    def post(self, request):
        pass