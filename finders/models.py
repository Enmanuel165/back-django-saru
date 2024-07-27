from django.db import models

# Create your models here.
class Finder(models.Model):
    email = models.EmailField(default=str, unique=True)
    password = models.CharField(max_length=200)
    type_acot = models.CharField(
        max_length=1, 
        choices=[
            ('P', 'Personal'),
            ('F', 'Familiar')    
        ],
        default='P'
    )
    
    def __str__(self) -> str:
        return self.email