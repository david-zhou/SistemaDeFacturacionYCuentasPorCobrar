from django.db import models

# Create your models here.
class Producto(models.Model):
	Nombre = models.CharField(max_length = 50)
	Clave = models.CharField(primary_key = True, max_length = 12)
	Unidad_de_medida = models.CharField(max_length = 10)
	Descripcion = models.CharField(max_length = 50)
	Precio = models.DecimalField(max_digits = 8, decimal_places = 2)
	Activo = models.BooleanField()
	Tipo_PS = (
                ('P','Producto'),
                ('S','Servicio'),
        )
	Tipo=models.CharField(max_length=1,choices=Tipo_PS)

class Dolar_peso(models.Model):
    valor=models.FloatField()
    fecha=models.DateTimeField(primary_key=True)
