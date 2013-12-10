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
from datetime import datetime

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
	arreglo = datos.split(",")
	fecha = datetime.now()
	# 0 id cliente
	# fecha hora
	# 1 monto
	# 2 saldo
	# status
	# tipo cambio
	if arreglo[3]=='D':
		# hacer la conversion
		dolar = Dolar_peso.objects.raw("Select top 1 valor from principal_Dolar_peso order by fecha desc")
		dolarFloat = float(dolar[0].valor)
		saldo = float(arreglo[2])
		saldo = saldo * dolarFloat
	else:
		saldo = float(arreglo[2])

	clave= int(arreglo[0])
	monto = float(arreglo[1][1:])
	if saldo >= monto:
		saldo=monto
		status = 'L'
	else:
		status = 'P'

	f = Factura(Clave_Cliente_id=clave, Fecha_Hora=fecha, Monto=monto, Saldo=saldo, Status=status, Tipo_Cambio='P')
	f.save()
	
	numFac = Factura.objects.raw("Select Numero_Factura from principal_Factura order by Fecha_Hora desc")
	numfac2 = int(numFac[0].Numero_Factura)
	
	l=int((len(arreglo)-4)/3)
	i = 4
	for x in range(0,l):
		claveProd = arreglo[i]
		i=i+1
		cant = float(arreglo[i])
		i=i+1
		precio = float(arreglo[i])
		i=i+1
		df = Detalle_Factura(Numero_Factura_id=numfac2, Producto_id= claveProd, Cantidad = cant, Precio_Unitario = precio)
		df.save()
		
	# 3 P|D
	#
	# 4 clave producto
	# 5 cantidad
	# 6 precio unitario
	
	return HttpResponseRedirect("/Seleccionar_ClienteFacturacion")


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
		Facturas = Clientes.objects.raw("Select C.Clave_Cliente, C.RFC, F.Numero_Factura, C.Clave_Cliente, Fecha_Hora, Monto, Saldo, CASE F.Status WHEN 'C' THEN 'Cancelada' WHEN 'L' THEN 'Liquidada' WHEN 'P' THEN 'Pendiente' END as Estatus FROM principal_Factura F INNER JOIN principal_Clientes C ON C.Clave_Cliente= F.Clave_Cliente_id")
	elif Status=='T':
		Facturas = Clientes.objects.raw("Select C.Clave_Cliente, C.RFC, F.Numero_Factura, C.Clave_Cliente, Fecha_Hora, Monto, Saldo, CASE F.Status WHEN 'C' THEN 'Cancelada' WHEN 'L' THEN 'Liquidada' WHEN 'P' THEN 'Pendiente' END as Estatus FROM principal_Factura F INNER JOIN principal_Clientes C ON C.Clave_Cliente= F.Clave_Cliente_id WHERE Fecha_Hora >'"+FechaInicio+"' AND Fecha_Hora <'"+FechaFinal+"'")
	elif Status=='C':
		Facturas = Clientes.objects.raw("Select C.Clave_Cliente, C.RFC, F.Numero_Factura, C.Clave_Cliente, Fecha_Hora, Monto, Saldo, CASE F.Status WHEN 'C' THEN 'Cancelada' WHEN 'L' THEN 'Liquidada' WHEN 'P' THEN 'Pendiente' END as Estatus FROM principal_Factura F INNER JOIN principal_Clientes C ON C.Clave_Cliente= F.Clave_Cliente_id WHERE Fecha_Hora >'"+FechaInicio+"' AND Fecha_Hora <'"+FechaFinal+"' AND Status='C'")
	elif Status=='P':
		Facturas = Clientes.objects.raw("Select C.Clave_Cliente, C.RFC, F.Numero_Factura, C.Clave_Cliente, Fecha_Hora, Monto, Saldo, CASE F.Status WHEN 'C' THEN 'Cancelada' WHEN 'L' THEN 'Liquidada' WHEN 'P' THEN 'Pendiente' END as Estatus FROM principal_Factura F INNER JOIN principal_Clientes C ON C.Clave_Cliente= F.Clave_Cliente_id WHERE Fecha_Hora >'"+FechaInicio+"' AND Fecha_Hora <'"+FechaFinal+"'AND Status='P'")
	elif Status=='L':
		Facturas = Clientes.objects.raw("Select C.Clave_Cliente, C.RFC, F.Numero_Factura, C.Clave_Cliente, Fecha_Hora, Monto, Saldo, CASE F.Status WHEN 'C' THEN 'Cancelada' WHEN 'L' THEN 'Liquidada' WHEN 'P' THEN 'Pendiente' END as Estatus FROM principal_Factura F INNER JOIN principal_Clientes C ON C.Clave_Cliente= F.Clave_Cliente_id WHERE Fecha_Hora >'"+FechaInicio+"' AND Fecha_Hora <'"+FechaFinal+"' AND Status='L'")
	else:
		Facturas = Clientes.objects.raw("Select C.Clave_Cliente, C.RFC, F.Numero_Factura, C.Clave_Cliente, Fecha_Hora, Monto, Saldo, CASE F.Status WHEN 'C' THEN 'Cancelada' WHEN 'L' THEN 'Liquidada' WHEN 'P' THEN 'Pendiente' END as Estatus FROM principal_Factura F INNER JOIN principal_Clientes C ON C.Clave_Cliente= F.Clave_Cliente_id")

	return render_to_response("Reporte_Facturas.html", {"Facturas":Facturas} , context_instance = RequestContext(request))

def v_Reporte_Estado(request):
	return render_to_response("Reporte_Estado.html" , context_instance = RequestContext(request))