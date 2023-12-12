from django import forms
from .models import Producto_Proteccion, Producto_almacen

class FormsProducto_Proteccion(forms.ModelForm):
    class Meta:
        model = Producto_Proteccion
        fields = '__all__'
    
class FormsProducto_almacen(forms.ModelForm):
    class meta:
        model = Producto_almacen
        field = '__all__'
        