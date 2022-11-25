from django.db import models


# Create your models here.
class Promocode(models.Model):

    """Promocode model"""

    # # alphanumeric = RegexValidator(
    # #     r"^[0-9a-zA-Z]*$", "Only alphanumeric characters are allowed."
    # # )
    code = models.CharField(max_length=10, unique=True)
    # # , validators=[alphanumeric])
    value = models.IntegerField(default=50)
    minimum_amount = models.IntegerField(default=10)
    valid_till_date = models.DateField()
    active = models.BooleanField(default=True)
