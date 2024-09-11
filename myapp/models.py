import datetime
from email.policy import default
from wsgiref.validate import validator
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.


class con(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()

class sup(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=100)

class fback(models.Model):
    des = models.TextField()
    score = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0)
                                ]
                                )

    def __str__(self):
        return str(self.pk)


class catagory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    categories = models.ForeignKey(catagory, on_delete=models.CASCADE, default=1)
    desc = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')


class Order(models.Model):
    orderid = models.IntegerField(default=0)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)

class recipie(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    desc = models.TextField(default='', null=True, blank=True)

class totalorder(models.Model):
    orderid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50 ,default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    totalamount=models.IntegerField(default='')


class captcha(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/captcha')

    

    
