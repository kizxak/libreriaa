from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Libros


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
