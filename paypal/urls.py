from django.urls import path
from . import views
from django.urls import include
from . import views


urlpatterns = [
    path("payments/", views.payments, name="payments"),
    path("payment_processing", views.payment_1, name="payment_processing"),
    path('process_order/', views.processOrder, name="process_order"),
]