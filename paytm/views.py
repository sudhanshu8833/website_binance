from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
from paytm import checksum
from shop.models import User1
import time
MERCHANT_KEY='x&Iog9XRoBP6r6hB'
amount=0


def payments(request):
    return render(request,"paytm/payments.html")



def payment_1(request):
    if request.method=="POST":
        amount=request.POST['amount']
    param_dict={

            'MID': 'luxrst14122371794696',
            'ORDER_ID': str(time.time()),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': 'WEB',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/paytm/handlerequest/',

    }

    param_dict['CHECKSUMHASH']=checksum.generate_checksum(param_dict,MERCHANT_KEY)
    print(param_dict)
    return  render(request, 'paytm/paytm.html', {'param_dict': param_dict})
    # return render(request, 'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    form=request.POST
    response_dict={}
    print(form)
    for i in form.keys():
        response_dict[i]=form[i]
        print(i)
        if i== 'CHECKSUMHASH':
            Checksum=form[i]
    print(response_dict)
    verify=checksum.verify_checksum(response_dict, MERCHANT_KEY, Checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            
            current_user=request.user
            actual_user=User1.objects.get(username=current_user)
            actual_user.credit+=actual_user.credit+amount
            actual_user.save()
            messages.success(request, f"Payment Successful, credits has been added...!")
            return redirect('index')

        else:
            print('order was not successful because'+response_dict['RESPMSG'])
            messages.error(request, f"Payment Unsuccessful because of {response_dict['RESPMSG']}")
            return redirect('index')

    return render(request,'paytm/paymentstatus.html',{'response':response_dict})