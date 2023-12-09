from django.shortcuts import render
from django.http import HttpResponse
from .models import Libros


# Create your views here.
def listar_libros(request):
    libros = Libros.objects.all()
    return render(request, "listar_libros.html", {"libros": libros})
