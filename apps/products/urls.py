from django.urls import path
from .views import (
    CreateProductAPIView,
    ActiveProductListAPIView,
    AllProductListAPIView,
    SingleProductAPIView,
    UpdateStockAPIView,
    DeleteProductAPIView,
    ProductStatsAPIView,
    ProductValueAPIView,
)
urlpatterns = [
    path('products/create/', CreateProductAPIView.as_view()),
    path('products/active/', ActiveProductListAPIView.as_view()),
    path('products/all/', AllProductListAPIView.as_view()),
    path('products/<int:id>/', SingleProductAPIView.as_view()),
    path("products/<int:id>/update-stock/", UpdateStockAPIView.as_view()),
    path("products/<int:id>/delete/", DeleteProductAPIView.as_view()),
    path("products/stats/", ProductStatsAPIView.as_view()),
    path("products/value/", ProductValueAPIView.as_view()),
]
