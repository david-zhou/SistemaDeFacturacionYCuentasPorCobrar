from django.db import models

# Create your models here.
class Producto(models.Model):
	Nombre = models.CharField(max_length = 50)
	Clave = models.IntegerField(Field.primary_key = true)
	Unidad_de_medida = CharField(max_length = 10)
	Descripcion = CharField(max_length = 50)
	Precio = models.DecimalField(decimal_places = 2)
	Activo = models.BooleanField()

