from django import forms
from principal.models import Producto
from principal.models import Clientes
from principal.models import Factura
from principal.models import Pagos

class ProductosForm(forms.ModelForm):
	class Meta:
		model = Producto

class ClientesForm(forms.ModelForm):
	class Meta:
		model = Clientes

class FacturaForm(forms.ModelForm):
	class Meta:
		model = Factura

class PagosForm(forms.ModelForm):
	class Meta:
		model = Pagos
