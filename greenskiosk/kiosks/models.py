from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class KioskOwner(models.Model):
    GENDER = (
        ("m", "male"),
        ("f", "female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.get_full_name()


class Kiosk(models.Model):
    owner = models.ForeignKey(KioskOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=28)
    date_opened = models.DateField()
    street_address = models.CharField(max_length=100)
    currency = models.CharField(max_length=8)
    phone_number = models.IntegerField()
    business_type = models.CharField(max_length=28)

    def __str__(self):
        return self.name

