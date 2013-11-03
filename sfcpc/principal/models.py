from django.db import models

# Create your models here.
class Dolar_peso(models.Model):
    valor=models.FloatField()
    fecha=models.DateTimeField(primary_key=True)
