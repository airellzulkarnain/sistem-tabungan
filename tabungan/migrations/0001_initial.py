# Generated by Django 3.2.9 on 2021-12-03 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0004_auto_20211203_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('target', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('freq_bill', models.SmallIntegerField(default=1)),
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
