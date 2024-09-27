from django.db import models
#Create your models here.
class Todo(models.Model):
    Title=models.CharField(max_length=255)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Contact(models.Model):  
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    message=models.TextField()  