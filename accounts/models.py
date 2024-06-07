from django.db import models
# Create your models here.

class Account(models.Model):
    email = models.EmailField(default=str)
    password = models.CharField(max_length=200)
    type_acot = models.CharField(
        max_length=1, 
        choices=[
            ('P', 'Personal'),
            ('F', 'Familiar')    
        ],
        default='P'
    )
    status = models.CharField(
        max_length=1, 
        choices=[
            ('A', 'Activado'),
            ('D', 'Desactivado')    
        ],
        default='A'
    )
    ivr = models.CharField(max_length=20)
    months = models.TextField()
    consul = models.TextField()
    cas = models.TextField()
    
    def __str__(self) -> str:
        return self.email
    