# Generated by Django 4.1.3 on 2022-11-21 08:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_comment'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basket',
            new_name='Cart',
        ),
        migrations.RenameModel(
            old_name='BasketItem',
            new_name='CartItem',
        ),
    ]