from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class DetalleProducto(models.Model):
    producto = models.OneToOneField('Producto', on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    dimensiones = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Relación Muchos a Uno: Un producto pertenece a una categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Relación Muchos a Muchos: Un producto puede tener varias etiquetas
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    # Detalles (Uno a Uno)
    # No se necesita aquí explícitamente porque lo definimos en DetalleProducto
    # pero se puede acceder como: producto.detalleproducto

    def __str__(self):
        return self.nombre
