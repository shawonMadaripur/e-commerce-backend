from rest_framework import serializers
from django.contrib.auth.models import User 

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Assuming User model is imported
        fields = ['username', 'first_name', 'last_name', 'email', 'password']  


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)