from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    last_login = models.DateTimeField()
    online_status = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.username}, last login : {self.last_login}"

class Saving(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    freq_bill = models.SmallIntegerField(default=1)

class Transaction(models.Model):
    saver_name = models.ForeignKey(User, on_delete=models.CASCADE)
    saving_name = models.ForeignKey(Saving, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateTimeField()