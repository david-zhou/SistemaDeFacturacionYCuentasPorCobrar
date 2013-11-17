# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.models import Factura
from principal.forms import FacturaForm
from principal.forms import ClientesForm
from principal.models import Producto
from principal.forms import ProductosForm
from principal.models import Dolar_peso
from principal.models import Detalle_Factura
from principal.models import Pagos
from principal.models import Estado_Ciudad
from principal.forms import Estado_CiudadForm
from principal.models import Clientes


def index(request):
	return render_to_response("index.html" , context_instance = RequestContext(request))

def Factura(request):
	return render_to_response("Factura.html" , context_instance = RequestContext(request))

def Clientes(request):
		return render_to_response("Clientes.html" , context_instance = RequestContext(request))

def Agregar_Estado_Ciudad(request):
	if request.method == "POST":
		formulario = Estado_CiudadForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Agregar_Estado_Ciudad")
	else:
		formulario = Estado_CiudadForm()

	return render_to_response("Agregar_Estado_Ciudad.html", {"formulario":formulario}, context_instance=RequestContext(request))


def Clientes_Alta(request):
	if request.method == "POST":
		formulario = ClientesForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Clientes_Alta")
	else:
		formulario = ClientesForm()
	return render_to_response("Clientes_Alta.html", {"formulario":formulario} , context_instance = RequestContext(request))

def Clientes_Baja(request):
	if request.method == "POST":
		formulario = ClientesForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Clientes_Baja")
	else:
		formulario = ClientesForm()
	return render_to_response("Clientes_Baja.html", {"formulario":formulario} , context_instance = RequestContext(request))

def Seleccionar_Cliente(request,Nombre_Cliente,RFC_Cliente):
	productos = Clientes.objects.all()
	#if Nombre_Cliente == "":
	#	Cliente = Clientes.objects.filter(RFC = RFC_Cliente)
	#elif RFC_Cliente == "":
	#	Cliente = Clientes.objects.filter(Nombres = Nombre_Cliente)
	#else:
	#	Cliente = Clientes.objects.filter(RFC = RFC_Cliente).filter(Nombres = Nombre_Cliente)
	return render_to_response("Seleccionar_Cliente.html" ,{"productos":productos}, context_instance = RequestContext(request))


def Clientes_Cambio(request, id_Cliente):
	Cliente = Clientes.objects.get(pk = id_Cliente)
	if request.method == "POST":
		formulario = ClientesForm(request.POST, instance = Cliente)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Clientes_Cambio")
	else:
		formulario = ProductoForm(instance=Cliente)
	return render_to_response("Clientes_Cambio.html", {"formulario":formulario}, context_instance = RequestContext(request))

def Pagos(request):
	return render_to_response("Pagos.html" , context_instance = RequestContext(request))

def Productos(request):
	return render_to_response("Productos.html" , context_instance = RequestContext(request))

def Productos_Alta(request):
	if request.method == "POST":
		formulario = ProductosForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Productos_Alta")
	else:
		formulario = ProductosForm()
	return render_to_response("Productos_Alta.html", {"formulario":formulario} , context_instance = RequestContext(request))


def Productos_Baja(request):
	if request.method == "POST":
		formulario = ProductosForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Productos_Baja")
	else:
		formulario = ProductosForm()
	return render_to_response("Productos_Baja.html", {"formulario":formulario} , context_instance = RequestContext(request))

def Productos_Cambio(request):
	if request.method == "POST":
		formulario = ProductosForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Productos_Cambio")
	else:
		formulario = ProductosForm()
	return render_to_response("Productos_Cambio.html", {"formulario":formulario} , context_instance = RequestContext(request))


def Pagos_Factura(request):
	return render_to_response("Pagos_Factura.html" , context_instance = RequestContext(request))

def Pagos_Clientes(request):
	return render_to_response("Pagos_Clientes.html" , context_instance = RequestContext(request))