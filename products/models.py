# pylint: disable=E1101
"""Product model"""

import uuid
from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    """Store product model"""

    class Meta:
        """Meta for Product model"""

        permissions = (("can_edit", "can_delete"),)

    serial_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    product_name = models.CharField(
        max_length=200, validators=[RegexValidator("[~!@#$%^&*+-]", inverse_match=True)]
    )
    product_brand = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
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
        """Return total comments for product"""
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


class Promocode(models.Model):
    """Promocode"""

    alphanumeric = RegexValidator(
        r"^[0-9a-zA-Z]*$", "Only alphanumeric characters are allowed."
    )
    code = models.CharField(max_length=10, unique=True, validators=[alphanumeric])
    value = models.IntegerField(default=50)
    valid_till_date = models.DateField()
    active = models.BooleanField(default=True)
    is_applied = models.BooleanField(default=False)

    def is_active(self):
        """Checks if a promocode is active"""
        if self.valid_till_date > date.today():
            is_active = True
        else:
            is_active = False

        if self.active is True:
            is_active = True
        else:
            is_active = False
        return is_active
