# Generated by Django 4.1.3 on 2022-11-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='images/avatar.jpeg', upload_to='images/'),
        ),
    ]
