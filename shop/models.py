from django.db import models
from django.db.models.fields import DateField, IntegerField
from django.forms import DateTimeInput

class User1(models.Model):
    username=models.CharField(max_length=50,default='SOME STRING')
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)
    phone=models.IntegerField(default='999')
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 
    group=models.IntegerField(default='0')


class orders(models.Model):
    symbol=models.CharField(max_length=100,default='SOME STRING')
    price_in=models.FloatField(default=0)
    time_in=models.DateTimeField(default=DateTimeInput)
    order_type=models.CharField(max_length=100,default='SOME STRING')

class positions(models.Model):
    symbol=models.CharField(max_length=100,default='SOME STRING')
    price_in=models.FloatField(default=0)
    time_in=models.DateTimeField(default=DateTimeInput)
    order_type=models.CharField(max_length=100,default='SOME STRING')
    current_pl=models.FloatField(default=0)

class groups(models.Model):
    num=models.IntegerField(default='0')
    profit=models.FloatField(default=0)
    position_size=models.FloatField(default=0)