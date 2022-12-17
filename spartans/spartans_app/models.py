# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    ci = models.CharField(db_column='CI', max_length=45)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45)  # Field name made lowercase.
    fechanac = models.DateField(db_column='FechaNac')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Detallefactura(models.Model):
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    producto_idproducto = models.OneToOneField('Producto', models.DO_NOTHING, db_column='producto_idProducto', primary_key=True)  # Field name made lowercase.
    factura_idfactura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='factura_idFactura')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detallefactura'
        unique_together = (('producto_idproducto', 'factura_idfactura'),)


class Dolarbcv(models.Model):
    fecha = models.DateTimeField(db_column='Fecha', primary_key=True)  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dolarbcv'


class Empleado(models.Model):
    idempleado = models.AutoField(db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'


class Factura(models.Model):
    idfactura = models.AutoField(db_column='idFactura', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    tipopago = models.CharField(db_column='TipoPago', max_length=45)  # Field name made lowercase.
    iva = models.FloatField(db_column='IVA')  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_idEmpleado')  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_idCliente')  # Field name made lowercase.
    dolarbcv_fecha = models.ForeignKey(Dolarbcv, models.DO_NOTHING, db_column='dolarbcv_Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45)  # Field name made lowercase.
    consola = models.CharField(db_column='Consola', max_length=45)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=45)  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio')  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    imagen = models.CharField(db_column='Imagen', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'
