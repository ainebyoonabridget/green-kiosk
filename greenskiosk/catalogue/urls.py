from django.urls import path
from . import views
from .views import products_list
from .views import upload_product
from .views import product_description
# product_description


urlpatterns = [
    path('products/', products_list, name='products_list'),
    path ("products/<int:product_id>/",product_description, name="product_description"),
    path("products/upload/", upload_product, name="product-uploads"),
  
]
