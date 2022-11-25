# pylint: disable=E1101
"""Product model"""

import uuid

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse

# from userprofile.models import UserProfile


class Product(models.Model):
    """Store product model"""

    class Meta:
        permissions = (("can_edit", "can_delete"),)

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
        """Return total comments for product"""
        count = self.comments.aggregate(count=models.Count("comment"))["count"]

        if count is None:
            count = 0

        return count

    # def product_count(self):
    #     count_p = self.objects.all().count()

    #     # if count_p is None:
    #     #     count_p= 0

    #     print(count_p)

    # return count_p


class Comment(models.Model):
    """Users can leave product comments"""

    # class Meta:
    #     app_label = "Comment"

    comment = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )


# class Promocode(models.Model):
#     """Promocode"""

#     # alphanumeric = RegexValidator(
#     #     r"^[0-9a-zA-Z]*$", "Only alphanumeric characters are allowed."
#     # )
#     code = models.CharField(max_length=10, unique=True)
#     # , validators=[alphanumeric])
#     value = models.IntegerField(default=50)
#     valid_till_date = models.DateField()
#     # minimum_amount = models.IntegerField(default=10)
#     active = models.BooleanField(default=True)
