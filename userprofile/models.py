"""User app"""
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Use email instead of username"""

    def create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """creates a superuser"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class UserProfile(AbstractUser):
    """User model"""

    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    full_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=100, null=True)
    post_code = models.CharField(max_length=30, null=True)
    avatar = models.ImageField(upload_to='images', default= 'images/avatar.jpeg')

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["full_name", "address", "city", "country", "post_code"]

    objects = UserProfileManager()

    def __str__(self):
        return f"{self.full_name}"

    def get_absolute_url(self):
        return reverse("user_profile")
