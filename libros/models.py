# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Libros(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    autor = models.CharField(max_length=255, blank=True, null=True)
    editorial = models.CharField(max_length=255, blank=True, null=True)
    fecha_publicacion = models.IntegerField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libros'


class Socios(models.Model):
    id_socio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios'


class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_socio = models.ForeignKey(Socios, models.DO_NOTHING, db_column='id_socio', blank=True, null=True)
    fecha_venta = models.DateField(blank=True, null=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'


class VentasLibros(models.Model):
    id_venta = models.OneToOneField(Ventas, models.DO_NOTHING, db_column='id_venta', primary_key=True)  # The composite primary key (id_venta, id_libro) found, that is not supported. The first column is selected.
    id_libro = models.ForeignKey(Libros, models.DO_NOTHING, db_column='id_libro')
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_libros'
        unique_together = (('id_venta', 'id_libro'),)
