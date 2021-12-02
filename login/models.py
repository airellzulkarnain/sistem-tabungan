from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15)
    last_login = models.DateTimeField()
    online_status = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.username}, last login : {self.last_login}"
