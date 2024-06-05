from django.db import models
# Create your models here.

class Account(models.Model):
    email = models.EmailField(default=str)
    password = models.CharField(max_length=200)
    type_acot = models.CharField(max_length=1)
    status = models.BooleanField(default=True)
    ivr = models.IntegerField(default=0)
    months = models.TextField()
    date = models.TextField()
    cas = models.TextField()
    
    def __str__(self) -> str:
        return self.email
    