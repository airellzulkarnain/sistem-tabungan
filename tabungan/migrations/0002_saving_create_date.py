# Generated by Django 3.2.9 on 2021-12-04 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabungan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saving',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 12, 4)),
        ),
    ]
