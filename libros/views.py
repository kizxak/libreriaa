# Importa funciones y clases necesarias de Django
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Libros,Socios
from .forms import LibrosForm,LoginForm
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required


# Create your views here.

# Vista para mostrar la lista de libros
def listar_libros(request):
    libros = Libros.objects.all()
    return render(request, "listar_libros.html", {"libros": libros})
#vista para eliminar libros
def eliminar_libro(request):
    if 'id' in request.GET:
        id_libro = request.GET['id']
        libro = get_object_or_404(Libros, id_libro=id_libro)
        if libro:
            libro.delete()

    return redirect("listar-libros")

#vista para editar los libros
def editarLibro(request, id):
    libro = get_object_or_404(Libros, id_libro=id)

    if request.method == 'POST':
        formulario = LibrosForm(request.POST, request.FILES, instance=libro)
        if formulario.is_valid():
            libro = formulario.save()
            return redirect('listar-libros')
    else:
        formulario = LibrosForm(instance=libro)

    return render(request, 'editar-libro.html', {'formulario': formulario, 'libro': libro})

#vista para agregar libros
def agregarLibro(request):
    if request.method == 'POST':
        formulario = LibrosForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar-libros')
    else:
        # Se crea un nuevo formulario
        formulario = LibrosForm()

    return render(request, 'agregar-libro.html', {'formulario': formulario})
#vista para que el usuario, Socio, pueda iniciar sesion
def login(request):
    form = LoginForm(request.POST)
    if request.method =="POST" and form.is_valid():
        #Asociamos las variables del formulario a variables de la función
        txt_correo = form.cleaned_data.get("txt_correo")
        txt_password = form.cleaned_data.get("txt_password")
        socios = Socios.objects.get(correo = txt_correo)
            #En caso de que la contraseña ingresada sea igual a la contraseña almacenada
        if socios.contrasena == txt_password:
            request.session['autenticado'] = True 
            request.session['correo'] = socios.correo 
            request.session['nombre_completo'] = socios.nombre +" "+ socios.apellido
            return redirect("listar-libros")
        else:
                form.add_error(None, 'Contraseña incorrecta')
    return render(request,"login.html",{"form" : form })

#Cerrar sesión
def logout(request):
    request.session.pop('autenticado',None)
    return redirect('login')
