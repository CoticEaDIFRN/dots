from django.contrib.admin import register, ModelAdmin, TabularInline, StackedInline
from .models import Colaborador, Vinculo, Registro, SolicitacaoApontamento, Apontamento


@register(Colaborador)
class ColaboradorAdmin(ModelAdmin):
    pass


@register(Vinculo)
class VinculoAdmin(ModelAdmin):
    pass


@register(Registro)
class RegistroAdmin(ModelAdmin):
    pass


@register(SolicitacaoApontamento)
class SolicitacaoApontamentoAdmin(ModelAdmin):
    pass


@register(Apontamento)
class ApontamentoAdmin(ModelAdmin):
    pass
