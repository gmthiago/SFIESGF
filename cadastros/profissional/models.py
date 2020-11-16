from django.db import models
from cadastros.usuarios.models import Usuarios


class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nome_professor = models.CharField(max_length=100, blank=False, null=True)
    telefone_professor = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    crefito = models.CharField(max_length=10, blank=False, null=True, verbose_name='CREFITO')
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=True, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
    usuario = models.ForeignKey(Usuarios, blank=True, null=False, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nome_professor

    class Meta:
        db_table = 'Professor'