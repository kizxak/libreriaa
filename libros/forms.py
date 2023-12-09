from django import forms
from .models import Libros
from django.forms import TextInput,NumberInput

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo','autor','editorial','fecha_publicacion','comentarios']
        widgets ={
            'titulo' : TextInput(attrs={'class': "form-control",'placeholder': 'Título'}),
            'autor':TextInput(attrs={'class': "form-control",'placeholder': 'Autor'}),
            'editorial':TextInput(attrs={'class': "form-control",'placeholder': 'Editorial'}),
            'fecha_publicacion':NumberInput(attrs={'class': "form-control",'placeholder': 'año de publicación'}),
            'comentarios':TextInput(attrs={'class': "form-control",'placeholder': 'comentarios'}),
        }