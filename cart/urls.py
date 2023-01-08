# pylint: disable=E0611
from django.urls import path

from .views import AddToCart, ViewCart

urlpatterns = [
    path("", ViewCart.as_view(), name="cart"),
    path("add/<uuid:product_id>/", AddToCart.as_view(), name="add_to_cart"),
]
