from django.db import models
from cadastros.profissional.models import Profissional

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome_paciente = models.CharField(max_length=100, blank=False, null=True)
    telefone_paciente = models.CharField(max_length=100, blank=False, null=True)
    profissional = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING)
    naturalidade = models.CharField(max_length=100, blank=False, null=True)
    estado_civil = models.CharField(max_length=100, blank=False, null=True)
    genero = models.CharField(max_length=100, blank=False, null=True)
    local_nascimento = models.CharField(max_length=100, blank=False, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    profissao = models.CharField(max_length=100, blank=False, null=True)
    endereco_comercial = models.CharField(max_length=100, blank=False, null=True)
    endereco_residencial = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=True, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nome_paciente

    class Meta:
        db_table = 'pacientes'