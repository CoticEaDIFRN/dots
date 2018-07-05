from django.contrib.admin import register, ModelAdmin, TabularInline, StackedInline
from django.contrib.auth.admin import UserAdmin
from .models import Colaborador, Vinculo, Registro, SolicitacaoApontamento, Apontamento

register(Colaborador, UserAdmin)


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
