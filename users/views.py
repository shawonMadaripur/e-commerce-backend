from django.shortcuts import render
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User


# Create your views here.

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response("successfully created", status=201)
        return Response(serializer.errors, status=400)
    
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Implement login logic here
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"message": "Login successful"}, status=200)
            return Response({"error": "Invalid credentials"}, status=400)
        return Response(serializer.errors, status=400)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=200)