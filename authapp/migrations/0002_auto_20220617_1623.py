# Generated by Django 3.2.13 on 2022-06-17 13:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users_avatar'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 19, 13, 23, 47, 695590, tzinfo=utc)),
        ),
    ]