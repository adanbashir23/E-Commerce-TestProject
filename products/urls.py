"""Products/urls"""
from django.urls import path

from .views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetail,
    ProductListView,
    ProductUpdateView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<uuid:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("<uuid:pk>/update/", ProductUpdateView.as_view(), name="product_edit"),
    path("<uuid:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
