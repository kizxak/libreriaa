from django import forms
from .models import Libros , Socios
from django.forms import TextInput,DateField

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo','autor','editorial','fecha_publicacion']
        widgets ={
            'titulo' : TextInput(attrs={'class': "form-control",'placeholder': 'Título'}),
            'autor':TextInput(attrs={'class': "form-control",'placeholder': 'Autor'}),
            'editorial':TextInput(attrs={'class': "form-control",'placeholder': 'Editorial'}),
            'fecha_publicación':DateField(attrs={'class': "form-control",'placeholder': 'Precio'}),
        }