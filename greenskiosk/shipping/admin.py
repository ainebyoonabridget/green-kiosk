from django.contrib import admin
from .models import DispenserCoolerBox,Delivery,ShippingProvider
# Register your models here.
admin.site.register(DispenserCoolerBox)
admin.site.register(ShippingProvider)
admin.site.register(Delivery)