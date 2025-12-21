from rest_framework import serializers
from .models import Product, Carosel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CaroselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carosel
        fields = '__all__'