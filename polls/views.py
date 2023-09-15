from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ShopSerializers
from .models import ShopModel
from rest_framework import generics
# Create your views here.

class GetShop(generics.ListAPIView):
      queryset = ShopModel.objects.all()
      serializer_class = ShopSerializers

class CreateShop(generics.CreateAPIView):
      queryset = ShopModel.objects.all()
      serializer_class = ShopSerializers
    
class GetCreateShop(generics.ListCreateAPIView):
      queryset = ShopModel.objects.all()
      serializer_class = ShopSerializers

class DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
      queryset = ShopModel.objects.all()
      serializer_class = ShopSerializers