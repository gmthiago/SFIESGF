# Generated by Django 3.1.2 on 2020-11-16 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id_professor', models.AutoField(primary_key=True, serialize=False)),
                ('nome_professor', models.CharField(max_length=100, null=True)),
                ('telefone_professor', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('crefito', models.CharField(max_length=10, null=True, verbose_name='CREFITO')),
                ('status', models.CharField(choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO'), ('EXCLUIDO', 'EXCLUIDO')], default='ATIVO', max_length=10, null=True, verbose_name='Status')),
                ('data_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuarios')),
            ],
            options={
                'db_table': 'Professor',
            },
        ),
    ]
