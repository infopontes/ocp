from area.models import *


class Localidades(models.Model):
    nome = models.CharField(max_length=50)
    lote_id = models.ForeignKey(Lotes, on_delete=models.CASCADE, verbose_name='Lote')

    class Meta:
        verbose_name = 'Localidade'
        verbose_name_plural = 'Localidades'
        ordering = ['nome',]
    
    def __str__(self):
        return self.id + ' - ' + self.nome