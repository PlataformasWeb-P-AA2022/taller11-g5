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
                
    def obtener_costo_departamentos(self):
        valor = 0;
        for t in self.departamentos.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo NumeroTelefonico
            valor = valor + t.costo_departamento
        return valor

    def obtener_cantidad_cuartos(self):
        """
        """
        valor = 0;
        for t in self.departamentos.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo NumeroTelefonico
            valor = valor + t.numero_cuartos
        return valor

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo_departamento = models.DecimalField(max_length=100)
    numero_cuartos = models.IntegerField(max_digits=100, decimal_places=2)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %f" % (self.nombre_propietario, self.costo_departamento)