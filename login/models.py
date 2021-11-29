from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    last_login = models.DateTimeField()
    online_status = models.BinaryField(default=0)

class Tabungan(models.Model):
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pass