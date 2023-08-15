"""Products/urls"""
from django.urls import path

from .views import (  # CommentDataView,; CommentView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetail,
    ProductListView,
    ProductSearchResultsView,
    ProductUpdateView,
    create_comment,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<uuid:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("<uuid:pk>/update/", ProductUpdateView.as_view(), name="product_edit"),
    path("<uuid:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("search/", ProductSearchResultsView.as_view(), name="product_search"),
    path("comment", create_comment, name="comment"),
    # path("<uuid:pk>/comments-view", CommentDataView.as_view(), name="comment_data"),
]
                