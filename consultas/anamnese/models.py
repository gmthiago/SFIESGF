from django.db import models
from cadastros.pacientes.models import Pacientes
from cadastros.profissional.models import Profissional


class Anamnese(models.Model):
    id_anamnese = models.AutoField(primary_key=True)
    historia_clinica = models.CharField(max_length=1000, blank=False, null=True)
    exame_clinico_funcional = models.CharField(max_length=1000, blank=False, null=True)
    exames_complementares = models.CharField(max_length=1000, blank=False, null=True)
    diagnostico = models.CharField(max_length=1000, blank=False, null=True)
    plano_terapeutico = models.CharField(max_length=1000, blank=False, null=True)
    evolucao = models.CharField(max_length=1000, blank=False, null=True)
    profissional = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Pacientes, on_delete=models.DO_NOTHING)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=True, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.historia_clinica

    class Meta:
        db_table = 'anamnese'
