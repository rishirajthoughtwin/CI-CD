from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    team = models.CharField(max_length=100)