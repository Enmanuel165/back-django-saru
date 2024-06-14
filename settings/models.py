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
    find_2024 = models.BooleanField(default=False)
    months_2024 = models.TextField(default='0')
    find_2025 = models.BooleanField(default=False)
    months_2025 = models.TextField(default='0')
    timing = models.IntegerField()
    