from django.db import models

# Create your models here.
class flight(models.Model):
    tipo = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=tipo)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre