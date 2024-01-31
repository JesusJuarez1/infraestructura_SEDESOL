# Generated by Django 4.2.7 on 2024-01-31 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import obras.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ObraPublica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_mids', models.CharField(max_length=255)),
                ('nombre_obra', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=255)),
                ('municipio', models.CharField(choices=[('', '------'), ('1', 'Apozol'), ('2', 'Apulco'), ('3', 'Atolinga'), ('4', 'Benito Juárez'), ('5', 'Calera'), ('6', 'Cañitas de Felipe Pescador'), ('7', 'Concepción del Oro'), ('8', 'Cuauhtémoc'), ('9', 'Chalchihuites'), ('10', 'Fresnillo'), ('11', 'Trinidad García de la Cadena'), ('12', 'Genaro Codina'), ('13', 'General Enrique Estrada'), ('14', 'General Francisco R. Murguía'), ('15', 'El Plateado de Joaquín Amaro'), ('16', 'General Pánfilo Natera'), ('17', 'Guadalupe'), ('18', 'Huanusco'), ('19', 'Jalpa'), ('20', 'Jerez'), ('21', 'Jiménez del Teul'), ('22', 'Juan Aldama'), ('23', 'Juchipila'), ('24', 'Loreto'), ('25', 'Luis Moya'), ('26', 'Mazapil'), ('27', 'Melchor Ocampo'), ('28', 'Mezquital del Oro'), ('29', 'Miguel Auza'), ('30', 'Momax'), ('31', 'Monte Escobedo'), ('32', 'Morelos'), ('33', 'Moyahua de Estrada'), ('34', 'Nochistlán de Mejía'), ('35', 'Noria de Ángeles'), ('36', 'Ojocaliente'), ('37', 'Pánuco'), ('38', 'Pinos'), ('39', 'Río Grande'), ('40', 'Sain Alto'), ('41', 'El Salvador'), ('42', 'Sombrerete'), ('43', 'Susticacán'), ('44', 'Tabasco'), ('45', 'Tepechitlán'), ('46', 'Tepetongo'), ('47', 'Teul de González Ortega'), ('48', 'Tlaltenango de Sánchez Román'), ('49', 'Valparaíso'), ('50', 'Vetagrande'), ('51', 'Villa de Cos'), ('52', 'Villa García'), ('53', 'Villa González Ortega'), ('54', 'Villa Hidalgo'), ('55', 'Villanueva'), ('56', 'Zacatecas'), ('57', 'Trancoso'), ('58', 'Santa María de la Paz')], max_length=2, verbose_name='Municipio')),
                ('localidad', models.CharField(max_length=150)),
                ('finalizado', models.BooleanField(default=False)),
                ('designado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EvidenciasObrasPublicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to=obras.models.upload_to_directory_obras)),
                ('es_proceso', models.BooleanField(default=True)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.obrapublica')),
            ],
        ),
    ]
