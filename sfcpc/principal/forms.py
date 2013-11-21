from django import forms
from principal.models import Producto
from principal.models import Clientes
from principal.models import Factura
from principal.models import Pagos
from principal.models import Estado_Ciudad

class ProductosForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = ("Activo")
	def __init__(self, *args, **kwargs):
                user = kwargs.pop('user','')
                super(ProductosForm, self).__init__(*args, **kwargs)

class ProductosBajasForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = ("Activo")
	def __init__(self, *args, **kwargs):
                user = kwargs.pop('user','')
                super(ProductosBajasForm, self).__init__(*args, **kwargs)
                self.fields['Clave_Producto'].widget.attrs['disabled']=True
                self.fields['Tipo'].widget.attrs['disabled']=True
                self.fields['Nombre'].widget.attrs['disabled']=True
                self.fields['Unidad_de_medida'].widget.attrs['disabled']=True
                self.fields['Descripcion'].widget.attrs['disabled']=True
                self.fields['Precio'].widget.attrs['disabled']=True
                

class ClientesForm(forms.ModelForm):
	class Meta:
		model = Clientes
		exclude = ("Activo")
	def __init__(self, *args, **kwargs):
                user = kwargs.pop('user','')
                super(ClientesForm, self).__init__(*args, **kwargs)
                #self.fields['Estado_Ciudad']=forms.ModelChoiceField(queryset=Estado_Ciudad.objects.values('Nombre_Estado','Nombre_Ciudad'))

class ClientesBajasForm(forms.ModelForm):
	class Meta:
		model = Clientes
		exclude = ("Activo")
	def __init__(self, *args, **kwargs):
                user = kwargs.pop('user','')
                super(ClientesBajasForm, self).__init__(*args, **kwargs)
                self.fields['RFC'].widget.attrs['disabled']=True
                self.fields['Fisico_Moral'].widget.attrs['disabled']=True
                self.fields['Nombres'].widget.attrs['disabled']=True
                self.fields['Apellidos'].widget.attrs['disabled']=True
                self.fields['Calle'].widget.attrs['disabled']=True
                self.fields['Numero_interior'].widget.attrs['disabled']=True
                self.fields['Numero_exterior'].widget.attrs['disabled']=True
                self.fields['Colonia'].widget.attrs['disabled']=True
                self.fields['CP'].widget.attrs['disabled']=True
                self.fields['Estado_Ciudad'].widget.attrs['disabled']=True
                self.fields['Cliente_Moroso'].widget.attrs['disabled']=True
                self.fields['Limite_Credito'].widget.attrs['disabled']=True


class FacturaForm(forms.ModelForm):
	class Meta:
		model = Factura

class PagosForm(forms.ModelForm):
	class Meta:
		model = Pagos

class Estado_CiudadForm(forms.ModelForm):
	class Meta:
		model = Estado_Ciudad
