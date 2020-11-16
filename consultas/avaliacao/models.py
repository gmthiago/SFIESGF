from django.db import models
from cadastros.pacientes.models import Pacientes
from cadastros.profissional.models import Professor
from cadastros.supervisor.models import Supervisor


class Avaliacao(models.Model):
    id_avaliacao_aluno = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.DO_NOTHING)
    avaliacao_upload = models.FileField(upload_to='', default='', verbose_name="Upload da Avaliação")
    observacoes = models.CharField(max_length=1000, blank=False, null=False, verbose_name="Observações")
    ciclo = models.CharField(max_length=1000, blank=False, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.DO_NOTHING)
    alunoa = models.CharField(max_length=100, blank=False, null=True, verbose_name="Aluno A")
    alunob = models.CharField(max_length=100, blank=True, null=False, verbose_name="Aluno B")
    alunoc = models.CharField(max_length=100, blank=True, null=False, verbose_name="Aluno C")
    alunod = models.CharField(max_length=100, blank=True, null=False, verbose_name="Aluno D")
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=True, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nome_aluno

    class Meta:
        db_table = 'avaliacao'