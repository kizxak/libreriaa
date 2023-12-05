from django import forms
import .models import Libros , Socios
from django.forms import TextInput,DateField

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo','autor','editorial','fecha_publicacion']
        widgets ={
            'titulo' : TextInput(attrs={'class': "form-control",'placeholder': 'Título'}),
            'autor':TextInput(attrs={'class': "form-control",'placeholder': 'Autor'}),
            'editorial':TextInput(attrs={'class': "form-control",'placeholder': 'Editorial'}),
            'fecha_publicación':DateInput(attrs={'class': "form-control",'placeholder': 'Precio'}),
        }