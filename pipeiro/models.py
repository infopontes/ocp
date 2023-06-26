from django.db import models


from manancial.models import Mananciais


class Pipeiros(models.Model):
    
    STATUS_CHOICES = (
        ("A", "Ativo"),
        ("I", "Inativo"),
        ("S", "Suspenso")
    )
    
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    nome = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nome')
    cnh = models.CharField(max_length=50, blank=False, null=False, verbose_name='CNH')
    foto_pipeiro = models.ImageField(verbose_name='Foto Pipeiro', upload_to='pipeiros')
    celular = models.CharField(max_length=14, verbose_name='Celular')
    placa = models.CharField(max_length=8, blank=False, null=False, verbose_name='Placa')
    foto_veiculo = models.ImageField(verbose_name='Foto Veículo', upload_to='veiculos')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False, default="I", verbose_name="Status")
    
    manancial_id = models.ForeignKey(Mananciais, on_delete=models.CASCADE, verbose_name='Mananciais')

    class Meta:
        verbose_name = 'Pipeiro'
        verbose_name_plural = 'Pipeiros'
        ordering = ['nome', 'placa']
    
    def __str__(self):
        return self.nome + ' - ' + self.placa
