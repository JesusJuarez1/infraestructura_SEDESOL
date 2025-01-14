import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

MUNICIPIOS = [
    ('', '------'),
    ('1', 'Apozol'),
    ('2', 'Apulco'),
    ('3', 'Atolinga'),
    ('4', 'Benito Juárez'),
    ('5', 'Calera'),
    ('6', 'Cañitas de Felipe Pescador'),
    ('7', 'Concepción del Oro'),
    ('8', 'Cuauhtémoc'),
    ('9', 'Chalchihuites'),
    ('10', 'Fresnillo'),
    ('11', 'Trinidad García de la Cadena'),
    ('12', 'Genaro Codina'),
    ('13', 'General Enrique Estrada'),
    ('14', 'General Francisco R. Murguía'),
    ('15', 'El Plateado de Joaquín Amaro'),
    ('16', 'General Pánfilo Natera'),
    ('17', 'Guadalupe'),
    ('18', 'Huanusco'),
    ('19', 'Jalpa'),
    ('20', 'Jerez'),
    ('21', 'Jiménez del Teul'),
    ('22', 'Juan Aldama'),
    ('23', 'Juchipila'),
    ('24', 'Loreto'),
    ('25', 'Luis Moya'),
    ('26', 'Mazapil'),
    ('27', 'Melchor Ocampo'),
    ('28', 'Mezquital del Oro'),
    ('29', 'Miguel Auza'),
    ('30', 'Momax'),
    ('31', 'Monte Escobedo'),
    ('32', 'Morelos'),
    ('33', 'Moyahua de Estrada'),
    ('34', 'Nochistlán de Mejía'),
    ('35', 'Noria de Ángeles'),
    ('36', 'Ojocaliente'),
    ('37', 'Pánuco'),
    ('38', 'Pinos'),
    ('39', 'Río Grande'),
    ('40', 'Sain Alto'),
    ('41', 'El Salvador'),
    ('42', 'Sombrerete'),
    ('43', 'Susticacán'),
    ('44', 'Tabasco'),
    ('45', 'Tepechitlán'),
    ('46', 'Tepetongo'),
    ('47', 'Teul de González Ortega'),
    ('48', 'Tlaltenango de Sánchez Román'),
    ('49', 'Valparaíso'),
    ('50', 'Vetagrande'),
    ('51', 'Villa de Cos'),
    ('52', 'Villa García'),
    ('53', 'Villa González Ortega'),
    ('54', 'Villa Hidalgo'),
    ('55', 'Villanueva'),
    ('56', 'Zacatecas'),
    ('57', 'Trancoso'),
    ('58', 'Santa María de la Paz'),
]

class ObraPublica(models.Model):
    folio_mids = models.CharField(max_length=255)
    designado = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_obra = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=255)
    municipio = models.CharField('Municipio', max_length=2, choices=MUNICIPIOS)
    localidad = models.CharField(max_length=150)
    finalizado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.folio_mids}"
        

def upload_to_directory_obras(instance, filename):
    # "obras/proceso" o "obras/terminacion"
    subfolder = 'proceso' if instance.es_proceso else 'terminacion'
    
    # Añadir una carpeta con la fecha actual para organizar por fecha
    current_date = timezone.now().strftime('%Y-%m-%d')
    return os.path.join('obras', subfolder, current_date, filename)

class EvidenciasObrasPublicas(models.Model):
    obra = models.ForeignKey(ObraPublica, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=upload_to_directory_obras)
    es_proceso = models.BooleanField(default=True)

    def __str__(self):
        tipo = 'Proceso' if self.es_proceso else 'Terminación'
        return f"{tipo} - {self.imagen}"