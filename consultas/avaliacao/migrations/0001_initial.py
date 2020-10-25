# Generated by Django 3.1.2 on 2020-10-25 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profissional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id_avaliacao_aluno', models.AutoField(primary_key=True, serialize=False)),
                ('nome_aluno', models.CharField(max_length=100, null=True)),
                ('avaliacao', models.CharField(max_length=1000, null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('status', models.CharField(choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO'), ('EXCLUIDO', 'EXCLUIDO')], default='ATIVO', max_length=10, null=True, verbose_name='Status')),
                ('data_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profissional.profissional')),
            ],
            options={
                'db_table': 'avaliacao',
            },
        ),
    ]
