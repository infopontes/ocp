from area.models import *



class Municipios(models.Model):
    codigo = models.CharField(max_length=7, primary_key=True)
    nome = models.CharField(max_length=50)
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True, null = True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True, null = True)
    estado_id = models.ForeignKey(Estados, on_delete=models.CASCADE, verbose_name='Estados')
    
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['nome',]
    
    
    def __str__(self):
        return self.nome + ' - ' + self.codigo