# Generated by Django 3.2.13 on 2022-06-17 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20220617_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 19, 16, 46, 26, 408426, tzinfo=utc)),
        ),
    ]
