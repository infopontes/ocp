from django.db import models
from area.models import Municipios


class Mananciais(models.Model):
    
    STATUS_CHOICES = (
        ("A", "Ativo"),
        ("I", "Inativo"),
        ("S", "Suspenso")
    )
    
    gcda = models.CharField(max_length=6, verbose_name='GCDA')
    capacidade = models.PositiveIntegerField(verbose_name='Capacidade')
    latitude_decimal = models.CharField(max_length=20, verbose_name='Latitude')
    longitude_decimal = models.CharField(max_length=20, verbose_name='Longitude')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False, default="I", verbose_name="Status")
    
    municipio_id = models.ForeignKey(Municipios, on_delete=models.CASCADE, verbose_name='Município')

    class Meta:
        verbose_name = 'Manancial'
        verbose_name_plural = 'Mananciais'
        ordering = ['gcda',]
    
    def __str__(self):
        return self.municipio_id.nome + ': GCDA ' + self.gcda + ' - Capacidade ' + self.capacidade