# Generated by Django 4.1.3 on 2022-11-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_userprofile_managers_userprofile_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='images/avatar.jpeg', upload_to='images'),
        ),
    ]
