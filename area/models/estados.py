from area.models import *


class Estados(models.Model):
    uf = models.CharField(verbose_name='UF', max_length=2, primary_key=True)
    nome = models.CharField(verbose_name='Nome', max_length=50)
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True, null = True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True, null = True)
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['nome']
    
    
    def __str__(self):
        return self.nome + '/' + self.uf