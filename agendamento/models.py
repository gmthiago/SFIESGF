from django.db import models


class Agenda(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False, null=True)
    telefone = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    queixa = models.CharField(max_length=1000, blank=False, null=True)
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'agenda'


