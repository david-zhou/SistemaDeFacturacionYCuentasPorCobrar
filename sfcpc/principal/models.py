from django.db import models

# Create your models here.
class Producto(models.Model):
	Nombre = models.CharField(max_length = 50)
	Clave_Producto = models.CharField(primary_key = True, max_length = 12)
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

class Estado_Ciudad(models.Model):
	Clave_EstadoCiudad = models.AutoField(primary_key = True)
	Nombre_Estado = models.CharField(max_length = 30)
	Nombre_Ciudad = models.CharField(max_length = 30)
	class Meta:
		unique_together = ('Nombre_Ciudad', 'Nombre_Estado')

class Clientes(models.Model):
	Clave_Cliente = models.AutoField(primary_key = True)
	Nombres = models.CharField(max_length = 50)
	Apellidos = models.CharField(max_length = 50)
	RFC = models.CharField(max_length = 13)
	Calle = models.CharField(max_length = 50) 
	Numero_interior = models.IntegerField()
	Colonia = models.CharField(max_length = 50)
	Numero_exterior = models.IntegerField()
	CP = models.IntegerField()
	Estado_Ciudad = models.ForeignKey(Estado_Ciudad)
	Fisico_Moral = models.CharField(max_length = 1)
	class Meta:
		unique_together = ('RFC','Calle')

class Factura(models.Model):
	Numero_Factura = models.AutoField(primary_key = True)
	Clave_Cliente = models.ForeignKey(Clientes)
	Fecha_Hora = models.DateTimeField()
	Monto = models.DecimalField(max_digits = 8, decimal_places = 2)
	Saldo = models.DecimalField(max_digits = 8, decimal_places = 2)
	Tipo_Factura = (
                ('C','Cancelada'),
                ('L','Liquidada'),
                ('P','Pagada'),
        )
	Status = models.CharField(max_length=1,choices=Tipo_Factura)

class Pagos(models.Model):
	Clave_Pagos = models.AutoField(primary_key = True)
	Numero_Factura = models.ForeignKey(Factura)
	Fecha = models.DateTimeField()
	Pago = models.DecimalField(max_digits = 8, decimal_places = 2)
	class Meta:
		unique_together = ('Numero_Factura','Fecha')


class Detalle_Factura(models.Model):
	Clave_DetalleFactura = models.AutoField(primary_key = True)
	Numero_Factura = models.ForeignKey(Factura)
	Producto = models.ForeignKey(Producto)
	Cantidad = models.IntegerField()
	Precio_Unitario = models.DecimalField(max_digits = 8, decimal_places = 2)
	class Meta:
		unique_together = ('Numero_Factura','Producto')