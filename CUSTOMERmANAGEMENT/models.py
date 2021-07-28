from django.db import models
from datetime import datetime

# Create your models here.


class CUSTOMER(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    Email = models.EmailField()
    Date_Created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class PRODUCT(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY)
    Description = models.TextField()
    Date_Created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class ORDER(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    # Customer =
    # Product =
    Date_Created = models.DateTimeField(default=datetime.now)
    Status = models.CharField(max_length=200, choices=STATUS)
