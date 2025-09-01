from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='departments')


class Product(models.Model):
    product = models.CharField(max_length=100)

class ProdDesc(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.TextField()
    
