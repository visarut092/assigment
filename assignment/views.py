from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import CollectData
from .models import *
from test_project.settings import set_db

# Create your views here.
class GetDetailSalesProduct(APIView):
    def get(self, request):
        try:
            total_price = 0
            total_sales = 0
            product_name = request.GET.get('product_name')

            try:
                get_product = Product.objects.using(set_db).get(product_name = product_name)
                product_id = get_product.product_id
            except:
                product_id = 0

            if product_id != 0:
                get_sales = Sales.objects.using(set_db).filter(product_id = product_id)
                for sales in get_sales:
                    total_price += (sales.quantity * sales.price)
                    total_sales += sales.quantity
            res = {
                'msg' : True,
                'data' : {
                    'product_total_sales' : total_sales,
                    'product_total_price' : total_price
                }
            }
            return Response(res,status=status.HTTP_200_OK)
        except:
            return Response(False,status=status.HTTP_400_BAD_REQUEST)

class SalesLittle(APIView):
    def get(self, request):
        try:
            collect_data = CollectData()
            min_data = sorted(list(filter(lambda i : (i['product_total_sales'] > 0), collect_data)), key = lambda i : i['product_total_sales'])
            res = {
                'msg' : True,
                'data' : min_data[0]
            }
            return Response(res,status=status.HTTP_200_OK)
        except:
            return Response(False,status=status.HTTP_400_BAD_REQUEST)

class SalesLot(APIView):
    def get(self, request):
        try:
            collect_data = CollectData()
            min_data = sorted(list(filter(lambda i : (i['product_total_sales'] > 0), collect_data)), key = lambda i : (i['product_total_sales']),reverse=True)
            res = {
                'msg' : True,
                'data' : min_data[0]
            }
            return Response(res,status=status.HTTP_200_OK)
        except:
            return Response(False,status=status.HTTP_400_BAD_REQUEST)

class SalesZero(APIView):
    def get(self, request):
        try:
            collect_data = CollectData()
            min_data = list(filter(lambda i : (i['product_total_sales'] == 0), collect_data))
            res = {
                'msg' : True,
                'data' : min_data[0]
            }
            return Response(res,status=status.HTTP_200_OK)
        except:
            return Response(False,status=status.HTTP_400_BAD_REQUEST)