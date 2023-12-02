from django.shortcuts import render

# Create your views here.
def listar_libros(request):
    libros = Libros.objects.all()
    return render(request, "libros/listar_libros.html", {"libros": libros})
