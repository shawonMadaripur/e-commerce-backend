from rest_framework import serializers
from django.contrib.auth.models import User 

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Assuming User model is imported
        fields = ['username', 'first_name', 'last_name', 'email', 'password'] 

    def save(self):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user 


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)