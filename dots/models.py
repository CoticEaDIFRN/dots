from django.db.models import Model, CharField, DateField, PositiveSmallIntegerField, DateTimeField, TimeField, \
    TextField, FilePathField, BooleanField
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django_brfied.django_brfied.models import CPFField, ForeignKey


class Colaborador(AbstractBaseUser, PermissionsMixin):
    cpf = CPFField('CPF', primary_key=True)
    nome = CharField('Nome', max_length=250)
    is_staff = BooleanField('Admin', default=False,)
    is_active = BooleanField('Ativo', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'cpf'

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.nome

    @property
    def username(self):
        return self.cpf

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return "%s (%s)" % (self.nome, self.cpf)


class Vinculo(Model):
    colaborador = ForeignKey('Colaborador', Colaborador)
    inicio = DateField('Início do vínculo')
    fim = DateField('Fím do vínculo', null=True)
    carga_horaria = PositiveSmallIntegerField('Carga horária por mês', validators=[MaxValueValidator(168)])
    lotacao = CharField('Lotação', max_length=250, null=True, blank=True)
    descricao = CharField('Descrição', max_length=250, null=True, blank=True)

    @property
    def encerrado_em(self):
        return '%s' % self.fim if self.fim is not None else 'Vínculo ativo'

    class Meta:
        verbose_name = 'Vínculo'
        verbose_name_plural = 'Vínculos'

    def __str__(self):
        return "%s [%s-%s] %d/mês" % (self.colaborador, self.inicio, self.encerrado_em, self.carga_horaria)


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

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return "%s - %s - %s" % (self.vinculo, self.tipo, self.quando)


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

    class Meta:
        verbose_name = 'Solicitação de apontamento'
        verbose_name_plural = 'Solicitações de apontamentos'

    def __str__(self):
        return "%s - %s - %s" % (self.vinculo, self.tipo, self.quando)


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
    horas = TimeField('Contar como quantas horas?')

    class Meta:
        verbose_name = 'Apontamento'
        verbose_name_plural = 'Apontamentos'

    def __str__(self):
        return "%s - %s - %s" % (self.vinculo, self.tipo, self.quando)
