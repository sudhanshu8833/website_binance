from django.urls import path
from . import views
from django.urls import include
from . import views


urlpatterns = [
    path("payments/", views.payments, name="payments"),
    path("handlerequest/", views.handlerequest, name="handlerequest"),
    path("payment_processing", views.payment_1, name="payment_processing"),
    
]