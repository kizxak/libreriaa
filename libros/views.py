from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Libros
from .forms import LibrosForm
from django.urls import reverse


# Create your views here.
def listar_libros(request):
    libros = Libros.objects.all()
    return render(request, "listar_libros.html", {"libros": libros})

def eliminar_libro(request):
    if 'id' in request.GET:
        id_libro = request.GET['id']
        libro = get_object_or_404(Libros, id_libro=id_libro)
        if libro:
            libro.delete()

    return redirect("listar-libros")


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