from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(default=0.0)
    stock_actual = models.IntegerField(default=0)
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="productos",
        on_delete=models.CASCADE
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre