from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"bots/home.html")

def about(request):
    return render(request,"bots/about.html")

def contact(request):
    return render(request,"bots/contact.html")
