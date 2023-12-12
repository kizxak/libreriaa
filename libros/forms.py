#importaciones de modelos, formularios y widgets
from django import forms
from .models import Libros
from django.forms import TextInput,NumberInput

# Define un formulario basado en el modelo Libros
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
# Define un formulario de inicio de sesión       
class LoginForm(forms.Form):
    txt_correo  = forms.CharField()
    txt_password =forms.CharField(widget = forms.PasswordInput)
