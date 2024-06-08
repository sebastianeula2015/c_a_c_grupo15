from django.db import models

# Create your models here.
provincias = [
    [0, "Mendoza"],
    [1, "San Luis"],
    [2, "San Juan"],
    [3, "La Rioja"],
    [4, "Neuquen"],
]


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.apellido},{self.nombre} "


class Cliente(Persona):
    dni = models.IntegerField()
    provincia = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vendedor(Persona):
    nro_vendedor = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    vendedores = models.ManyToManyField('Vendedor')
    detalle_venta = models.ForeignKey('DetalleVenta', on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta del {self.fecha} para {self.cliente}"


class DetalleVenta(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} ({self.cantidad})"

class Proveedor(Persona):
    cuit = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

