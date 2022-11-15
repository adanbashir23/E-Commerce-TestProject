# pylint: disable=E1101
"""Product model"""

import uuid
from django.db import models

# from userprofile.models import UserProfile

# Create your models here.
from django.urls import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    """Store product model"""

    serial_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    product_name = models.CharField(max_length=200)
    product_brand = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=10)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    images = models.FileField(blank=True)

    def get_absolute_url(self):
        """define default url for an instance of product model"""
        return reverse("product_detail", kwargs={"pk": str(self.serial_number)})

    # class ProductImage(models.Model):
    #     """image model"""
    #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #     images = models.FileField(upload_to="images/")

    def comment_count(self):
        """Return total reviews for product"""
        count = self.comments.aggregate(count=models.Count("comment"))["count"]

        if count is None:
            count = 0

        return count


class Comment(models.Model):
    """Users can leave product comments"""

    comment = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
