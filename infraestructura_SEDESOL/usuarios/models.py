from django.db import models

class Beneficiario_Calentador(models.Model):
    id = models.AutoField(primary_key=True)
    folio_mids = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    nombres = models.CharField(max_length=100)
    municipio = models.CharField(max_length=150)
    localidad = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.apellido_paterno}, {self.nombres}"