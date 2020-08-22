from django.contrib import admin
from .models import Kiosk, KioskOwner
# Register your models here.

admin.site.register(KioskOwner)
admin.site.register(Kiosk)



