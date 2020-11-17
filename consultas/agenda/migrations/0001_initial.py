# Generated by Django 3.1.2 on 2020-11-16 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id_agendamento_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('telefone', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('principal_queixa', models.CharField(max_length=1000, null=True)),
                ('CID', models.CharField(max_length=1000, null=True)),
                ('diag_clinico', models.CharField(max_length=1000, null=True, verbose_name='Diagnóstico Clínico')),
                ('pedido_medico', models.FileField(default='', upload_to='', verbose_name='Pedido Médico')),
                ('data_agendamento', models.DateTimeField(blank=True, null=True)),
                ('alunoa', models.CharField(max_length=100, null=True, verbose_name='Aluno A')),
                ('alunob', models.CharField(blank=True, max_length=100, verbose_name='Aluno B')),
                ('alunoc', models.CharField(blank=True, max_length=100, verbose_name='Aluno C')),
                ('alunod', models.CharField(blank=True, max_length=100, verbose_name='Aluno D')),
                ('data_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pacientes.pacientes')),
            ],
            options={
                'db_table': 'agendap',
            },
        ),
    ]
