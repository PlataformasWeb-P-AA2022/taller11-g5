from django.db import models

# Create your models here.

class Edificio(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo) 
    def costo_no_mayor (self):
        valor = 0
        if(self.costo_departamento > 100000):
            valor

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo_departamento = models.DecimalField(max_length=100)
    numero_cuartos = models.IntegerField(max_digits=100, decimal_places=2)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %f" % (self.nombre_propietario, self.costo_departamento)