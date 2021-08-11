from django.db import models
from datetime import datetime

# Create your models here.

class TEST(models.Model):
    STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Others', 'Others'),
)
    Name = models.CharField(max_length = 100)
    Status = models.CharField(max_length=100, choices=STATUS)
    Date_Added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.Name
