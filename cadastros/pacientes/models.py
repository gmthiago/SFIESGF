from django.db import models


class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome_paciente = models.CharField(max_length=100, blank=False, null=True)
    telefone_paciente = models.CharField(max_length=100, blank=False, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=False, choices=(
        ('SOLTEIRO', 'SOLTEIRO'),
        ('CASADO', 'CASADO'),
        ('UNIAO ESTAVEL', 'UNIAO ESTAVEL'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('SEPARADO', 'SEPARADO'),
        ('OUTROS', 'OUTROS'),
    ))
    nacionalidade = models.CharField(max_length=100, blank=False, null=True)
    genero = models.CharField(max_length=15, blank=False, null=False, choices=(
        ('MASCULINO', 'MASCULINO'),
        ('FEMININO', 'FEMININO'),
        ('OUTROS', 'OUTROS'),
    ))
    cidade = models.CharField(max_length=100, blank=False, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    profissao = models.CharField(max_length=100, blank=True, null=False)
    endereco_comercial = models.CharField(max_length=100, blank=True, null=False)
    endereco_residencial = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=50, blank=True, null=False)
    nome_acompanhante = models.CharField(max_length=100, blank=True, null=False)
    diag_clinico = models.CharField(max_length=1000, blank=False, null=True, verbose_name='Diagnóstico Clínico')
    ch_faixa_etaria = models.CharField('Faixa Etária', max_length=11, default='', blank=False, null=True, choices=(
        ('ADULTO', 'ADULTO'),
        ('ADOLESCENTE', 'ADOLESCENTE'),
        ('CRIANÇA', 'CRIANÇA'),
    ))
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