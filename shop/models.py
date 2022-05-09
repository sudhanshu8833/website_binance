from django.db import models
from django.db.models.fields import DateField, IntegerField

class User1(models.Model):
    username=models.CharField(max_length=50,default='SOME STRING')
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)
    phone=models.IntegerField(default='999')
    fullname=models.CharField(max_length=50,default='SOME STRING')
    account_num=models.IntegerField(default='999')
    ifsc=models.CharField(max_length=50,default='SOME STRING')
    referral=models.IntegerField(default=0)
    another_referral=models.CharField(max_length=50)
    credit=models.IntegerField(default='999')
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 
    angel_API_keys=models.CharField(max_length=100,default='SOME STRING')
    angel_username=models.CharField(max_length=100,default='SOME STRING')
    angel_password=models.CharField(max_length=100, default='SOME STRING')
    security=models.IntegerField(default=0)
    profit=models.IntegerField(default=0)


class BOT1(models.Model):
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 
    Expiry_date=models.DateField()
    email=models.EmailField(max_length=50)
    Max_loss=models.IntegerField()

class BOT2(models.Model):
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 
    Expiry_date=models.DateField()
    email=models.EmailField(max_length=50)
    Max_loss=models.IntegerField()


class BOT3(models.Model):
    angel_API_keys=models.CharField(max_length=100,default='SOME STRING')
    username=models.CharField(max_length=100,default='SOME STRING')
    password=models.CharField(max_length=100, default='SOME STRING') 
    Expiry_date=models.DateField()
    email=models.EmailField(max_length=50)
    Max_loss=models.IntegerField()


class BOT4(models.Model):
    angel_API_keys=models.CharField(max_length=100,default='SOME STRING')
    username=models.CharField(max_length=100,default='SOME STRING')
    password=models.CharField(max_length=100, default='SOME STRING') 
    Expiry_date=models.DateField()
    email=models.EmailField(max_length=50)
    Max_loss=models.IntegerField()

class BOT(models.Model):
    Price=models.IntegerField()
    subscription_time=models.CharField(max_length=100) 
    description=models.CharField(max_length=5000) 
    title=models.CharField(max_length=50)
