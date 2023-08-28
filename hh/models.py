from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    note1=models.CharField(max_length=100)
    note2=models.CharField(max_length=100)
    note3=models.CharField(max_length=100)
    smell=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images/')

class AboutUs(models.Model):
    content=models.CharField(max_length=1000)

class TagLine(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
class Image(models.Model):
    img1=models.ImageField(upload_to='images/')
    img2=models.ImageField(upload_to='images/')

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)