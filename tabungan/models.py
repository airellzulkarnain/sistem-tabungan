from django.db import models
from login.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class Saving(models.Model):
    class Meta:
        unique_together = (('name', 'owned_by'), )
    name = models.CharField(max_length=15)
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_date = models.DateField()
    notice_every = models.CharField(max_length=6, default="bulan")
    jumlah_pembayaran = models.PositiveSmallIntegerField(default=10, validators=[MaxValueValidator(48), MinValueValidator(7)])
    status = models.CharField(max_length=12, default="belum lunas.")

class Transaction(models.Model):
    saver_name = models.ForeignKey(User, on_delete=models.CASCADE)
    saving_name = models.ForeignKey(Saving, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateTimeField()