from django.db import models
class Users(models.Model):
    Username=models.CharField(max_length=250)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=250)
    Name=models.CharField(max_length=250)
    Phone=models.CharField(max_length=250)