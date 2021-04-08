from rest_framework import serializers
from .models import Product
from .models import Category

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ('name','url_image', 'price', 'discount','category')