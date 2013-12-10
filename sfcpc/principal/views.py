# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.models import Factura
from principal.forms import FacturaForm
from principal.forms import ClientesForm
from principal.forms import ClientesBajasForm
from principal.models import Producto
from principal.forms import ProductosForm
from principal.forms import ProductosBajasForm
from principal.models import Dolar_peso
from principal.models import Detalle_Factura
from principal.models import Pagos
from principal.models import Estado_Ciudad
from principal.forms import Estado_CiudadForm
from principal.models import Clientes

def v_index(request):
	return render_to_response("index.html" , context_instance = RequestContext(request))

def v_Factura(request, id_Cliente, RFC_Cliente):
	p = Producto.objects.raw("Select * FROM principal_producto WHERE Activo = 1")
	return render_to_response("Factura.html" ,{"productos":p, "rfc":RFC_Cliente, "id_Cliente":id_Cliente}, context_instance = RequestContext(request))

def v_Clientes(request):
		return render_to_response("Clientes.html" , context_instance = RequestContext(request))

def v_Clientes_Alta(request):
	if request.method == "POST":
		formulario = ClientesForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Clientes_Alta")
	else:
		formulario = ClientesForm()
	return render_to_response("Clientes_Alta.html", {"formulario":formulario} , context_instance = RequestContext(request))

def v_Agregar_Estado_Ciudad(request):
	if request.method == "POST":
		formulario = Estado_CiudadForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Agregar_Estado_Ciudad")
	else:
		formulario = Estado_CiudadForm()

	return render_to_response("Agregar_Estado_Ciudad.html", {"formulario":formulario}, context_instance=RequestContext(request))


def v_Clientes_Baja(request, id_Cliente):
	Cliente = Clientes.objects.get(pk = id_Cliente)
	if request.method == "POST":
		formulario = ClientesBajasForm(request.POST, instance = Cliente)
		Clientes.objects.filter(pk = id_Cliente).update(Activo = 0)
		return HttpResponseRedirect("/Seleccionar_ClienteBaja")
	else:
		formulario = ClientesBajasForm(instance = Cliente)
	return render_to_response("Clientes_Baja.html", {"formulario":formulario} , context_instance = RequestContext(request))

def v_Seleccionar_Cliente(request,Nombre_Cliente,RFC_Cliente):
	if Nombre_Cliente =='null' and RFC_Cliente == 'null':
		Cliente = Clientes.objects.raw("Select * FROM principal_clientes WHERE Activo = 1")
	else:
		Cliente = Clientes.objects.raw("Select * FROM principal_clientes WHERE (Nombres LIKE '"'%%%%'+str(Nombre_Cliente)+'%%%%'"' OR RFC LIKE '"'%%%%'+str(RFC_Cliente)+'%%%%'"') AND Activo = 1")
	return render_to_response("Seleccionar_Cliente.html" ,{"Cliente":Cliente}, context_instance = RequestContext(request))

def v_Generar_Factura(request, datos):
	return render_to_response("Seleccionar_ClienteFacturacion.html", {"arreglo":datos}, context_instance = RequestContext(request))


def v_Seleccionar_ClienteBaja(request,Nombre_Cliente,RFC_Cliente):
	if Nombre_Cliente =='null' and RFC_Cliente == 'null':
		Cliente = Clientes.objects.raw("Select * FROM principal_clientes WHERE Activo = 1")
	else:
		Cliente = Clientes.objects.raw("Select * FROM principal_clientes WHERE (Nombres LIKE '"'%%%%'+str(Nombre_Cliente)+'%%%%'"' OR RFC LIKE '"'%%%%'+str(RFC_Cliente)+'%%%%'"') AND Activo = 1")
	return render_to_response("Seleccionar_ClienteBaja.html" ,{"Cliente":Cliente}, context_instance = RequestContext(request))

def v_Seleccionar_ClienteFacturacion(request,Nombre_Cliente,RFC_Cliente):
	if Nombre_Cliente =='null' and RFC_Cliente == 'null':
		Cliente = Clientes.objects.raw("Select * FROM principal_clientes WHERE Activo = 1")
	else:
		Cliente = Clientes.objects.raw("Select * FROM principal_clientes WHERE (Nombres LIKE '"'%%%%'+str(Nombre_Cliente)+'%%%%'"' OR RFC LIKE '"'%%%%'+str(RFC_Cliente)+'%%%%'"') AND Activo = 1")
	return render_to_response("Seleccionar_ClienteFacturacion.html" ,{"Cliente":Cliente}, context_instance = RequestContext(request))


def v_Clientes_Cambio(request, id_Cliente):
	Cliente = Clientes.objects.get(pk = id_Cliente)
	if request.method == "POST":
		formulario = ClientesForm(request.POST, instance = Cliente)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Seleccionar_Cliente")
	else:
		formulario = ClientesForm(instance=Cliente)
	return render_to_response("Clientes_Cambio.html", {"formulario":formulario}, context_instance = RequestContext(request))

def v_Pagos(request):
	return render_to_response("Pagos.html" , context_instance = RequestContext(request))

def v_Productos(request):
	return render_to_response("Productos.html" , context_instance = RequestContext(request))

def v_Productos_Alta(request):
	if request.method == "POST":
		formulario = ProductosForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Productos_Alta")
	else:
		formulario = ProductosForm()
	return render_to_response("Productos_Alta.html", {"formulario":formulario} , context_instance = RequestContext(request))


def v_Productos_Baja(request, id_Producto):
	p = Producto.objects.get(pk = id_Producto)
	if request.method == "POST":
		formulario = ProductosBajasForm(request.POST, instance = p)

		Producto.objects.filter(pk = id_Producto).update(Activo = 0)
		return HttpResponseRedirect("/Seleccionar_ProductoBaja")
	else:
		formulario = ProductosBajasForm(instance = p)
	return render_to_response("Productos_Baja.html", {"formulario":formulario} , context_instance = RequestContext(request))

def v_Productos_Cambio(request,id_Producto):
	p = Producto.objects.get(pk = id_Producto)
	if request.method == "POST":
		formulario = ProductosForm(request.POST, instance = p)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Seleccionar_Producto")
	else:
		formulario = ProductosForm(instance = p)
	return render_to_response("Productos_Cambio.html", {"formulario":formulario} , context_instance = RequestContext(request))

def v_Seleccionar_Producto(request,Nombre_Producto,Clave_Producto):
	if Nombre_Producto =='null' and Clave_Producto =='null':
		p = Producto.objects.raw("Select * FROM principal_producto WHERE Activo = 1")
	else:
		p = Producto.objects.raw("Select * FROM principal_producto WHERE (Nombre LIKE '"'%%%%'+str(Nombre_Producto)+'%%%%'"' OR Clave_Producto LIKE '"'%%%%'+str(Clave_Producto)+'%%%%'"') AND Activo = 1")	
	return render_to_response("Seleccionar_Producto.html", {"producto":p} , context_instance = RequestContext(request))


def v_Seleccionar_ProductoBaja(request,Nombre_Producto,Clave_Producto):
	if Nombre_Producto =='null' and Clave_Producto =='null':
		p = Producto.objects.raw("Select * FROM principal_producto WHERE Activo = 1")
	else:
		p = Producto.objects.raw("Select * FROM principal_producto WHERE (Nombre LIKE '"'%%%%'+str(Nombre_Producto)+'%%%%'"' OR Clave_Producto LIKE '"'%%%%'+str(Clave_Producto)+'%%%%'"') AND Activo = 1")
	return render_to_response("Seleccionar_ProductoBaja.html", {"producto":p} , context_instance = RequestContext(request))

def v_Pagos_Factura(request):
	return render_to_response("Pagos_Factura.html" , context_instance = RequestContext(request))

def v_Pagos_Clientes(request):
	return render_to_response("Pagos_Clientes.html" , context_instance = RequestContext(request))

def v_Reportes(request):
	return render_to_response("Reportes.html" , context_instance = RequestContext(request))

def v_Reporte_Facturas(request,FechaInicio,FechaFinal,Status):
	if FechaInicio =='null' and FechaFinal == 'null':
		Facturas = Factura.objects.raw("Select C.Clave_Cliente, C.RFC, F.Numero_Factura, C.Clave_Cliente, datetime(Fecha_Hora) as Fecha_Hora, Monto, Saldo, Status, Tipo_Cambio  FROM principal_Factura F INNER JOIN principal_Clientes C ON C.Clave_Cliente= F.Clave_Cliente_id ")
	elif Status=='T':
		Facturas = Factura.objects.raw("Select C.Clave_Cliente, C.RFC, F.Numero_Factura, C.Clave_Cliente, F.Fecha_Hora, F.Monto, F.Saldo, F.Status, F.Tipo_Cambio  FROM principal_Factura F INNER JOIN principal_Clientes C ON C.Clave_Cliente= F.Clave_Cliente_id WHERE Fecha_Hora >'"'%%%%'+str(FechaInicio)+'%%%%'"' and Fecha_Hora <'"'%%%%'+str(FechaFinal)+'%%%%'"'")
	elif Status=='C':
		Facturas = Clientes.objects.raw("Select * FROM principal_Factura WHERE Tipo_Factura = 'C' AND Fecha_Hora >'"'%%%%'+str(FechaInicio)+'%%%%'"' and Fecha_Hora <'"'%%%%'+str(FechaFinal)+'%%%%'"'")
	else:
		Facturas = Factura.objects.raw("Select F.Numero_Factura, datetime(F.Fecha_Hora) as Fecha_Hora, F.Monto, F.Saldo, F.Status, F.Tipo_Cambio  FROM principal_Factura F WHERE Fecha_Hora >'12-12-11' and Fecha_Hora <'12-12-14'")

	return render_to_response("Reporte_Facturas.html", {"Facturas":Facturas} , context_instance = RequestContext(request))

def v_Reporte_Estado(request):
	return render_to_response("Reporte_Estado.html" , context_instance = RequestContext(request))