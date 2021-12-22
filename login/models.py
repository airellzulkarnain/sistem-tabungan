from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.aggregates import Min

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15)
    last_login = models.DateTimeField()
    online_status = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])

    def __str__(self):
        return f"{self.username}, last login : {self.last_login}"
