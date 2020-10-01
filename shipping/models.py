from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ShippingProvider(models.Model):
    name = models.CharField(max_length=30)
    date_joined=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.IntegerField()
    transport_mode=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class DispenserCoolerBox(models.Model):
    box_number=models.IntegerField()
    location=models.CharField(max_length=30)
    unlock_code=models.IntegerField()
     
    def __str__(self):
        return self.box_number


class Delivery(models.Model):
    #order=models.ForeignKey(Order, on_delete=models.CASCADE)
    dispatch_time=models.DateTimeField()
    shipping_provider=models.ForeignKey(ShippingProvider, on_delete=models.CASCADE)
    cooler_box=models.CharField(max_length=30)

    
    def __str__(self):
        return self.order()
