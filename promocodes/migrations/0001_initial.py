# Generated by Django 4.1.3 on 2022-11-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Promocode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10, unique=True)),
                ("value", models.IntegerField(default=50)),
                ("minimum_amount", models.IntegerField(default=10)),
                ("valid_till_date", models.DateField()),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]