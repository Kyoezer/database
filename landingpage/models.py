# from turtle import back, title
from django.db import models

# Create your models here.
class landind_page(models.Model):
    binner = models.FileField(upload_to='videos/%Y/%m/%d/')

class logo(models.Model):
    logo = models.ImageField(upload_to='logo/%Y/%m/%d/')

class operate(models.Model):
    operate = models.TextField(max_length=200)

class copy_right(models.Model):
    copy = models.IntegerField()

class quote(models.Model):
    author = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True)
    quotes = models.TextField(max_length=200, blank=True)
    create_date = models.DateTimeField( auto_now_add=True, blank=True)
    

