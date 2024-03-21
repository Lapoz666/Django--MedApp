from django.db import models

class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)