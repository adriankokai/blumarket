from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .serializers import OrderSerializer
from rest_framework.parsers import JSONParser
import io
import json

# Create your views here.
def deserialize(json):
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    return data

@api_view(['POST'])
def place_order(request):
    data = json.dumps(request.data['order'])
    data = deserialize(bytes(data, encoding='utf8'))
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        order = serializer.save()
        return Response('placed order:', order.id)
    else:
        print(serializer.data)
        print(serializer.errors)
        return Response('failed to place order')

@api_view(['GET'])
def product(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print('products', serializer.data)
    return Response(serializer.data)
