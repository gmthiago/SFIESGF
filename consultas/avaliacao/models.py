from django.db import models
from cadastros.profissional.models import Profissional


class Avaliacao(models.Model):
    id_avaliacao_aluno = models.AutoField(primary_key=True)
    nome_aluno = models.CharField(max_length=100, blank=False, null=True)
    avaliacao = models.CharField(max_length=1000, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=True, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
    profissional = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nome_aluno

    class Meta:
        db_table = 'avaliacao'