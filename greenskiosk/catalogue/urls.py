from django.urls import path
from . import views
from .views import products_list
from .views import upload_product


urlpatterns = [
    path('products/', products_list, name='products_list'),
    path("products/upload/", upload_product, name="product-uploads")
]
