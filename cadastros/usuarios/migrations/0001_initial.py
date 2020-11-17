# Generated by Django 3.1.2 on 2020-11-16 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=40)),
                ('admnistrador', models.IntegerField(default=0)),
                ('administrador_super', models.IntegerField(default=0)),
                ('cadastra_usuario', models.IntegerField(default=0)),
                ('edita_usuario', models.IntegerField(default=0)),
                ('acessa_cadastro_usuario', models.IntegerField(default=0)),
                ('muda_status_usuario', models.IntegerField(default=0)),
                ('cadastra_paciente', models.IntegerField(default=0)),
                ('edita_paciente', models.IntegerField(default=0)),
                ('acessa_cadastro_paciente', models.IntegerField(default=0)),
                ('muda_status_paciente', models.IntegerField(default=0)),
                ('cadastra_profissional', models.IntegerField(default=0)),
                ('edita_profissional', models.IntegerField(default=0)),
                ('acessa_cadastro_profissional', models.IntegerField(default=0)),
                ('muda_status_profisisonal', models.IntegerField(default=0)),
                ('observacoes', models.TextField(blank=True, max_length=200)),
                ('status', models.CharField(default='ATIVO', max_length=10)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuarios', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('status', models.CharField(choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO'), ('EXCLUIDO', 'EXCLUIDO')], default='ATIVO', max_length=10, null=True, verbose_name='Status')),
                ('model_template', models.CharField(blank=True, max_length=100, null=True)),
                ('data_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('permissoes', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.permissoes')),
                ('usuario', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usuarios',
                'ordering': ('nome',),
            },
        ),
    ]
