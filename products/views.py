from django.shortcuts import render
from .models import Product, Carosel
from .serializers import ProductSerializer, CaroselSerializer
from rest_framework import viewsets 
from rest_framework.views import APIView 
from rest_framework.response import Response

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__icontains=category)
        return queryset
    

class CaroselViewSet(APIView):
    def post(self, request):
        form = CaroselSerializer(data=request.data)
        if form.is_valid():
            form.save()
            return Response("submitted successfully")
        return Response(form.errors, status=400)