from django.shortcuts import render
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User

# import for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # hsahing the password
            user.set_password(serializer.validated_data['password'])
            user.save()

            # Send welcome email
            email_subject = "Your Account Has Been Created successfully"
            email_body = render_to_string('email.html')
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # Implement login logic here
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"message": "Login successful"}, status=200)
            return Response({"error": "Invalid credentials"}, status=400)
        return Response(serializer.errors, status=400)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=200)