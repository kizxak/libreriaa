"""
URL configuration for libreria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importa el módulo 'admin'y el módulo 'path' para las rutas de la aplicación
from django.contrib import admin
from django.urls import path
from libros import views

# Lista de URL's que definen cómo se asignan las URL a las vistas
urlpatterns = [
    path('admin/', admin.site.urls),
    path("lista-libros/", views.listar_libros, name="listar-libros"),
    path("eliminar_libro/", views.eliminar_libro, name="eliminar-libro"),
    path('editar-libro/<int:id>/', views.editarLibro , name='editarLibro'),
    path('agregar-libro/', views.agregarLibro, name='agregarLibro'),
    path('login/',views.login,name="login"),
    path('logout/', views.logout, name="logout")
]
