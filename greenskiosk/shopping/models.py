from django.db import models
from django.contrib.auth.models import User
from catalogue.models import Product
from customers.models import Customer



# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    date_created = models.DateTimeField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2,default=1.00)
    status=models.CharField(max_length=50,null=True)

    
    def __str__(self):
        return self.status


class Payment(models.Model):
    payment_method = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_payment = models.DateTimeField()
    
    def __str__(self):
        return self.payment_method


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
        return self.status