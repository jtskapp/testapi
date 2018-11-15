from django.shortcuts import render
from api_v1.serializers import CustomerSerializer
from rest_framework import generics
from api_v1.models import Customer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

class CustomerCRView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

@api_view(['GET',])
def TotalCount(request):
    total_count = Customer.objects.all().count()
    data = {
        'total_count' : total_count
    }
    return Response(data)




    
