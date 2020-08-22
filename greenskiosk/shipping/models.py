from django.db import models
from django.contrib.auth.models import User
from shopping.models import Order


class ShippingProvider(models.Model):
    name = models.CharField(max_length=40)
    date_joined = models.DateField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    transport_mode = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

class DispenserCoolerBox(models.Model):
    box_number = models.IntegerField()
    location = models.CharField(max_length=50)
    unlock_code = models.IntegerField()
    
    def __str__(self):
        return self.box_number


class Delivery(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('shipping.ShippingProvider',on_delete=models.CASCADE)
    cooler_box = models.CharField(max_length=40)
    
    def __str__(self):
        return self.order
    