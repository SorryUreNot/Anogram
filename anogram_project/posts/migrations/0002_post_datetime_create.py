# Generated by Django 4.1 on 2022-09-17 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 16, 21, 8, 207164)),
        ),
    ]
