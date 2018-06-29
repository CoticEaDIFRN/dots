from django.db.models import Model, CharField, DateField, PositiveSmallIntegerField, DateTimeField, TextField, \
    FilePathField
from django.core.validators import MaxValueValidator
from django_brfied.django_brfied.models import CPFField, ForeignKey


class Colaborador(Model):
    cpf = CPFField()
    nome = CharField('Nome', max_length=250)


class Vinculo(Model):
    colaborador = ForeignKey('Colaborador', Colaborador)
    inicio = DateField('Início do vínculo')
    fim = DateField('Fím do vínculo', null=True)
    carga_horaria = PositiveSmallIntegerField('Carga horária por mês', validators=[MaxValueValidator(168)])
    unidade_organizacional = CharField('UOrg', max_length=250, null=True, blank=True)


class Registro(Model):
    ENTRADA = 'Entrada'
    SAIDA = 'Saída'
    TIPOS = [(ENTRADA, ENTRADA), (SAIDA, SAIDA)]

    # quem
    vinculo = ForeignKey('Vínculo', Vinculo)
    # quando
    quando = DateTimeField('Quando')
    # o que
    tipo = CharField('O quê', max_length=7, choices=TIPOS)


class SolicitacaoApontamento(Model):
    AUSENCIA = 'Ausência'
    INCONSISTENCIA = 'Inconsistência'
    TIPOS = [(AUSENCIA, AUSENCIA), (INCONSISTENCIA, INCONSISTENCIA)]

    # quem
    vinculo = ForeignKey('Vínculo', Vinculo)
    # o que
    tipo = CharField('Tipo', max_length=50, choices=TIPOS)
    # quando
    data_hora = DateTimeField('Quando')
    # onde
    local = CharField('Local', max_length=250, null=True, blank=True)
    # porque
    justificativa = TextField('Justificativa')
    # porque
    comprovante = FilePathField('Comprovante', null=True)


class Apontamento(Model):
    DEFERIDO = 'Deferido'
    PARCIAL = 'Parcialmente deferido'
    INDEFERIDO = 'Indeferido'
    DEFERIMENTOS = [(DEFERIDO, DEFERIDO), (INDEFERIDO, INDEFERIDO), (PARCIAL, PARCIAL)]

    # quem
    solicitacao = ForeignKey('Solicitação de apontamento', SolicitacaoApontamento)
    # o que
    deferimento = CharField('Deferimento', max_length=22, choices=DEFERIMENTOS)
    # porque deferiu/indeferiu
    justificativa = TextField('Justificativa')
    # quando
    data_hora = DateTimeField('Quando')
    # quanto
    horas = DateTimeField('Contar como quantas horas?')
