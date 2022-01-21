from django.contrib import admin
from inscricoes.models import Inscricao


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    ordering = ['nome']
    list_display = ('nome','dt_inscricao', 'email', 'participa_almoco')
    list_display_links = ('nome','dt_inscricao', 'email', 'participa_almoco')
