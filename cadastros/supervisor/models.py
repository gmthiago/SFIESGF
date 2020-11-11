from django.db import models

class Supervisor(models.Model):
    id_supervisor = models.AutoField(primary_key=True)
    nome_supervisor = models.CharField(max_length=100, blank=False, null=True)
    telefone_supervisor = models.CharField(max_length=100, blank=False, null=True)
    crefito = models.CharField(max_length=10, blank=False, null=True, verbose_name='CREFITO')
    email = models.EmailField(max_length=30, blank=False, unique=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=True, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nome_supervisor

    class Meta:
        db_table = 'supervisor'