from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
from shop.models import User1
import datetime
from django.http import JsonResponse
import json


def payments(request):
    return render(request,"paypal/payments.html")
def payment_1(request):
    if request.method=="POST":
        amount=request.POST['amount']

    return  render(request, 'paypal/paypal.html', {'amount': amount})



def processOrder(request):
    data=json.loads(request.body)
    total=float(data['form']['total'])
    current_user=request.user
    acttual_user=User1.objects.get(username=current_user)
    acttual_user.credit+=acttual_user.credit+total
    acttual_user.save()
    messages.success(request, f"Payment Successful, credits has been added...!")
    return redirect('index')
# def processOrder(request):
# 	data = json.loads(request.body)

# 	total = float(data['form']['total'])

# 	current_user=request.user
#     actual_user=User1.objects.get(username=current_user)
#     actual_user.credit+=actual_user.credit+amount
#     actual_user.save()
#     messages.success(request, f"Payment Successful, credits has been added...!")
#     return redirect('index')
