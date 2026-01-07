from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Avg, Count, Max, Min, F

from .models import Product
from .serializers import ProductSerializer


# 🔹 1. CREATE PRODUCT → objects.create()
class CreateProductAPIView(APIView):
    def post(self, request):
        product = Product.objects.create(
            name=request.data.get("name"),
            price=request.data.get("price"),
            stock=request.data.get("stock"),
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 🔹 2. LIST ACTIVE PRODUCTS → objects.filter()
class ActiveProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# 🔹 3. LIST ALL PRODUCTS → objects.all()
class AllProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# 🔹 4. GET SINGLE PRODUCT → objects.get()
class SingleProductAPIView(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class UpdateStockAPIView(APIView):
    def patch(self, request, id):
        Product.objects.filter(id=id).update(
            stock=F("stock") + request.data.get("quantity", 1)
        )
        return Response({"message": "Stock updated"})



class DeleteProductAPIView(APIView):
    def delete(self, request, id):
        Product.objects.filter(id=id).delete()
        return Response({"message": "Product deleted"})


class ProductStatsAPIView(APIView):
    def get(self, request):
        data = Product.objects.aggregate(
            total_products=Count("id"),
            total_stock=Sum("stock"),
            avg_price=Avg("price"),
            max_price=Max("price"),
            min_price=Min("price")
        )
        return Response(data)


class ProductValueAPIView(APIView):
    def get(self, request):
        products = Product.objects.annotate(
            total_value=F("price") * F("stock")
        ).values("name", "total_value")

        return Response(products)
