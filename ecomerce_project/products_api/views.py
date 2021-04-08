""" api views"""
from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
# Create your views here.

# @api_view(['GET'])
# def showemp(request):
#     if req.method=='GET':
#         results=Product.objects.all()
#         serialize=ProductSerializer(results,many=True)
#         return response(serialize.data)

class Product_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        results=Product.objects.all()
        serialize=ProductSerializer(results,many=True)
        
        return Response(serialize.data)

    # def post(self, request, format=None):
    #     serializer = PostSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)