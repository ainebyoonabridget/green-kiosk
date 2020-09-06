from django.contrib import admin
from .models import Product, ProductCategory,ProductReview,ProductSuplier
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductReview)
admin.site.register(ProductSuplier)

