from django.urls import path

from checkout.views import checkoutview, process_order

urlpatterns = [
    path("", process_order, name="checkout"),
    path("payment-complete/", checkoutview, name="checkout_complete"),
]
