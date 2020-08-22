from django.db import models
from django.contrib.auth.models import User
from catalogue.models import Product
from customers.models import Customer



# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    date_created = models.DateTimeField()
    p_name = models.CharField(max_length=7, default='proucts')

    
    def __str__(self):
        return self.p_name


class Payment(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=30)
    order = models.ForeignKey('Order',on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_payment = models.DateTimeField()
    
    def __str__(self):
        return self.customer


class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateTimeField()
    status = models.CharField(max_length=40)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='+')
    delivery_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('shipping.ShippingProvider', on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=5, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.order_number