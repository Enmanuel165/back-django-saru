from django.db import models

# Create your models here.

class Settings(models.Model):
    name = models.CharField(max_length=50)
    type_search = models.CharField(
        max_length=1,
        default='G',
        choices=[
            ('P', 'Personal'), 
            ('F', 'Familiar'), 
            ('G', 'General'), 
            ('D', 'Desactivado')
        ]
    )
    timing = models.IntegerField()
    