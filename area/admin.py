from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Estados)
class EstadosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome', 'uf')
    
@admin.register(Municipios)
class MunicipiosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')
    search_fields = ('nome',)


@admin.register(Lotes)
class LotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Localidades)
class LocalidadesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)