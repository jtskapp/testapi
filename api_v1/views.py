from django.shortcuts import render
from api_v1.serializers import CustomerSerializer
from rest_framework import generics
from api_v1.models import Customer

# Create your views here.

class CustomerCRView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
