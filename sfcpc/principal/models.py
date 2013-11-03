from django.db import models

# Create your models here.
<<<<<<< HEAD
class Producto(models.Model):
	Nombre = models.CharField(max_length = 50)
	Clave = models.IntegerField(Field.primary_key = true)
	Unidad_de_medida = CharField(max_length = 10)
	Descripcion = CharField(max_length = 50)
	Precio = models.DecimalField(decimal_places = 2)
	Activo = models.BooleanField()

=======
class Dolar_peso(models.Model):
    valor=models.FloatField()
    fecha=models.DateTimeField(primary_key=True)
>>>>>>> 839765bc0dafb601d9100963f62de6517868f8aa
