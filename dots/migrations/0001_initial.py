# Generated by Django 2.0.6 on 2018-06-29 23:12

import django.core.validators
from django.db import migrations, models
import django_brfied.django_brfied.models
import django_brfied.django_brfied.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apontamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deferimento', models.CharField(choices=[('Deferido', 'Deferido'), ('Indeferido', 'Indeferido'), ('Parcialmente deferido', 'Parcialmente deferido')], max_length=22, verbose_name='Deferimento')),
                ('justificativa', models.TextField(verbose_name='Justificativa')),
                ('data_hora', models.DateTimeField(verbose_name='Quando')),
                ('horas', models.DateTimeField(verbose_name='Contar como quantas horas?')),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', django_brfied.django_brfied.models.CPFField(mask='999.999.999-00', max_length=11, validators=[django_brfied.django_brfied.validators.CPFValidator()], verbose_name='')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quando', models.DateTimeField(verbose_name='Quando')),
                ('tipo', models.CharField(choices=[('Entrada', 'Entrada'), ('Saída', 'Saída')], max_length=7, verbose_name='O quê')),
            ],
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
        ),
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(verbose_name='Início do vínculo')),
                ('fim', models.DateField(null=True, verbose_name='Fím do vínculo')),
                ('carga_horaria', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(168)], verbose_name='Carga horária por mês')),
                ('unidade_organizacional', models.CharField(blank=True, max_length=250, null=True, verbose_name='UOrg')),
                ('colaborador', django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='dots.Colaborador', verbose_name='Colaborador')),
            ],
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
    ]
