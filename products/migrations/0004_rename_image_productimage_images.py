# Generated by Django 4.1.3 on 2022-11-11 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='images',
        ),
    ]
