# Generated by Django 3.2.9 on 2021-12-05 06:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20211203_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='online_status',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
    ]
