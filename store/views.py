from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['POST'])
def place_order(request):
    pass

@api_view(['GET'])
def product(request):
    product = Product.objects.all()[0]
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
