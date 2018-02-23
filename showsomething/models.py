# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Buyers(models.Model):
    buyerFirstName = models.CharField(max_length=100)
    buyerlastName = models.CharField(max_length=100)
    nationalCode = models.CharField(max_length=100)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=100)
    mobileNumber = models.CharField(max_length=100)
    requireDeliveryTime = models.CharField(max_length=100)
    Deliveryaddress = models.TextField()
    deliveryMode = models.CharField(max_length=100)
    genderPressent =models.CharField(max_length=100,null=True)
   
    def __str__(self):
        return self.buyerFirstName+" "+ self.buyerlastName
