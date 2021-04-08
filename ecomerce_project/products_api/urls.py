"""'''Api Urls'''"""
from django.urls import path
from products_api.views import *

app_name = 'products_api'

urlpatterns = [
    path('showapi',Product_APIView.as_view()),
]