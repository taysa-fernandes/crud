from django.contrib import admin


from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

admin.site.register(Pessoa, PessoaAdmin)
