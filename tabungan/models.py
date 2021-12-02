from django.db import models
from login.models import User

# Create your models here.
class Saving(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    freq_bill = models.SmallIntegerField(default=1)
    status = models.CharField(max_length=12, default="belum lunas.")

class Transaction(models.Model):
    saver_name = models.ForeignKey(User, on_delete=models.CASCADE)
    saving_name = models.ForeignKey(Saving, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateTimeField()