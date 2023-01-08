# Generated by Django 4.1.3 on 2022-11-27 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(
                max_length=200,
                validators=[
                    django.core.validators.RegexValidator(
                        "[~!@#$%^&*+-]", inverse_match=True
                    )
                ],
            ),
        ),
    ]
