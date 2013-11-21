from django import forms
from principal.models import Producto
from principal.models import Clientes
from principal.models import Factura
from principal.models import Pagos
from principal.models import Estado_Ciudad

class ProductosForm(forms.ModelForm):
	class Meta:
		model = Producto

class ClientesForm(forms.ModelForm):
	class Meta:
		model = Clientes
	def __init__(self, *args, **kwargs):
                user = kwargs.pop('user','')
                super(ClientesForm, self).__init__(*args, **kwargs)
                self.fields['Estado_Ciudad']=forms.ModelChoiceField(queryset=Estado_Ciudad.objects.values('Nombre_Estado','Nombre_Ciudad'))

class FacturaForm(forms.ModelForm):
	class Meta:
		model = Factura

class PagosForm(forms.ModelForm):
	class Meta:
		model = Pagos

class Estado_CiudadForm(forms.ModelForm):
	class Meta:
		model = Estado_Ciudad
