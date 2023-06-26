from django.contrib import admin
from .models import Mananciais

@admin.register(Mananciais)
class ManancialAdmin(admin.ModelAdmin):
    list_display = ('gcda', 'status')
    search_fields = ('gcda', 'status')
    
