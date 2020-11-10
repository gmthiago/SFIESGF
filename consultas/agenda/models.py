from django.db import models
from cadastros.pacientes.models import Pacientes
from cadastros.profissional.models import Profissional


class Agenda(models.Model):
    id_agendamento_paciente = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.DO_NOTHING)
    telefone = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    principal_queixa = models.CharField(max_length=1000, blank=False, null=True)
    profissional = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING, null=False)
    data_agendamento = models.DateTimeField(blank=True, null=True)
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'agendap'