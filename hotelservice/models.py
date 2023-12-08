# models.py
from django.db import models

class Contactus(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    message=models.TextField()
