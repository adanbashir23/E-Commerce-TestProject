# Generated by Django 4.1.3 on 2022-11-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0004_alter_userprofile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="avatar",
            field=models.ImageField(
                default="https://res.cloudinary.com/dxmms7rbf/image/upload/v1660544735/samples/ecommerce/analog-classic.jpg",
                upload_to="images/",
            ),
        ),
    ]