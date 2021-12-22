# Generated by Django 4.0 on 2021-12-22 05:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('target', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_date', models.DateField()),
                ('jumlah_pembayaran', models.PositiveSmallIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(48), django.core.validators.MinValueValidator(7)])),
                ('status', models.CharField(default='belum lunas.', max_length=12)),
                ('owned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
            ],
            options={
                'unique_together': {('name', 'owned_by')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('payment_date', models.DateTimeField()),
                ('saver_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
                ('saving_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabungan.saving')),
            ],
        ),
    ]
