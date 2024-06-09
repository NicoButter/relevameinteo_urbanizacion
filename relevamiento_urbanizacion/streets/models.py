from django.db import models

class Localidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Street(models.Model):
    es_avenida = models.BooleanField(default=False)
    nombre = models.CharField(max_length=100)
    altura_inicial = models.IntegerField()
    altura_final = models.IntegerField()
    coordenadas_iniciales = models.CharField(max_length=255, blank=True, null=True)
    coordenadas_finales = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def longitud_en_metros(self):
        return self.altura_final / 100 if self.altura_final else 0

    def __str__(self):
        return f"{self.nombre} ({self.altura_inicial} - {self.altura_final})"
