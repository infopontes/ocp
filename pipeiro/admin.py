from django.contrib import admin
from .models import Pipeiros

@admin.register(Pipeiros)
class PipeiroAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'status')
    search_fields = ('cpf', 'nome', 'placa')