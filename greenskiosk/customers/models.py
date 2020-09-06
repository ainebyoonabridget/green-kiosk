from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    GENDER = (
        ("m", "male"),
        ("f","female")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    profile_picture = models.ImageField()
    
    def __str__(self):
        return self.user.get_full_name()

class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    notes = models.TextField()
    
    def __str__(self):
        return self.address
