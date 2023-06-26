from area.models import *


class Lotes(models.Model):
    nome = models.CharField(max_length=7)
    municipio_id = models.ForeignKey(Municipios, on_delete=models.CASCADE, verbose_name='Município')

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
        ordering = ['nome',]
    
    def __str__(self):
        return self.municipio_id.nome + ' - ' + self.nome