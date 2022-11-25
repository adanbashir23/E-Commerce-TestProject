# pylint: disable=E1101
"""userprofile/urls"""
from django.urls import path

from . import views

urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name="user_profile"),
]
