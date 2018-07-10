from django.contrib.admin import register, ModelAdmin, TabularInline, StackedInline
from django.contrib.auth.admin import UserAdmin
from .models import Colaborador, Vinculo, Registro, SolicitacaoApontamento, Apontamento

register(Colaborador, UserAdmin)


@register(Colaborador)
class ColaboradorAdmin(ModelAdmin):
    fields = ('cpf', 'nome', 'is_staff', 'is_active', 'is_superuser', 'groups')
    readonly_fields = ('last_login',)
    list_display = ('cpf', 'nome', 'is_staff', 'is_active', 'is_superuser', 'last_login')
    list_filter = ('is_staff', 'is_active', 'is_superuser')



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
