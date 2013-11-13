# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.models import Factura
from principal.forms import FacturaForm
from principal.models import Clientes
from principal.forms import ClientesForm
from principal.models import Producto
from principal.forms import ProductosForm

def index(request):
	return render_to_response("index.html" , context_instance = RequestContext(request))

def Factura(request):
	return render_to_response("Factura.html" , context_instance = RequestContext(request))

def Clientes(request):
		return render_to_response("Clientes.html" , context_instance = RequestContext(request))

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

def Clientes_Cambio(request):
	if request.method == "POST":
		formulario = ClientesForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Clientes_Cambio")
	else:
		formulario = ClientesForm()
	return render_to_response("Clientes_Cambio.html", {"formulario":formulario} , context_instance = RequestContext(request))

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