from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User 
# Create your views here.
from django.http import HttpResponse
# from .models import User1,BOT

def index(request):
    return render(request,"userbot/index.html")
