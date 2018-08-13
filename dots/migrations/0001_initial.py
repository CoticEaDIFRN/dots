from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django_brfied.django_brfied.models
import django_brfied.django_brfied.validators
from dots.migrations import criar_primeiro_colaborador


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('cpf', django_brfied.django_brfied.models.CPFField(mask='999.999.999-00', max_length=11, primary_key=True, serialize=False, validators=[django_brfied.django_brfied.validators.CPFValidator()], verbose_name='')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Apontamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deferimento', models.CharField(choices=[('Deferido', 'Deferido'), ('Indeferido', 'Indeferido'), ('Parcialmente deferido', 'Parcialmente deferido')], max_length=22, verbose_name='Deferimento')),
                ('justificativa', models.TextField(verbose_name='Justificativa')),
                ('data_hora', models.DateTimeField(verbose_name='Quando')),
                ('horas', models.TimeField(verbose_name='Contar como quantas horas?')),
            ],
            options={
                'verbose_name': 'Apontamento',
                'verbose_name_plural': 'Apontamentos',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quando', models.DateTimeField(verbose_name='Quando')),
                ('tipo', models.CharField(choices=[('Entrada', 'Entrada'), ('Saída', 'Saída')], max_length=7, verbose_name='O quê')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
        migrations.CreateModel(
            name='SolicitacaoApontamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Ausência', 'Ausência'), ('Inconsistência', 'Inconsistência')], max_length=50, verbose_name='Tipo')),
                ('data_hora', models.DateTimeField(verbose_name='Quando')),
                ('local', models.CharField(blank=True, max_length=250, null=True, verbose_name='Local')),
                ('justificativa', models.TextField(verbose_name='Justificativa')),
                ('comprovante', models.FilePathField(null=True, verbose_name='Comprovante')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(verbose_name='Início do vínculo')),
                ('fim', models.DateField(null=True, verbose_name='Fím do vínculo')),
                ('carga_horaria', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(168)], verbose_name='Carga horária por mês')),
                ('lotacao', models.CharField(blank=True, max_length=250, null=True, verbose_name='Lotação')),
                ('descricao', models.CharField(blank=True, max_length=250, null=True, verbose_name='Descrição')),
                ('colaborador', django_brfied.django_brfied.models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL, verbose_name='Colaborador')),
            ],
            options={
                'verbose_name': 'Vínculo',
                'verbose_name_plural': 'Vínculos',
            },
        ),
        migrations.AddField(
            model_name='solicitacaoapontamento',
            name='vinculo',
            field=django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='dots.Vinculo', verbose_name='Vínculo'),
        ),
        migrations.AddField(
            model_name='registro',
            name='vinculo',
            field=django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='dots.Vinculo', verbose_name='Vínculo'),
        ),
        migrations.AddField(
            model_name='apontamento',
            name='solicitacao',
            field=django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='dots.SolicitacaoApontamento', verbose_name='Solicitação de apontamento'),
        ),
        migrations.RunPython(
            criar_primeiro_colaborador
        ),
    ]
