from django.contrib.auth.models import User
from django.db import models


class Permissoes(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=40)

    admnistrador = models.IntegerField(default=0)
    administrador_super = models.IntegerField(default=0)

    cadastra_usuario = models.IntegerField(default=0)
    edita_usuario = models.IntegerField(default=0)
    acessa_cadastro_usuario = models.IntegerField(default=0)
    muda_status_usuario = models.IntegerField(default=0)

    cadastra_paciente = models.IntegerField(default=0)
    edita_paciente = models.IntegerField(default=0)
    acessa_cadastro_paciente = models.IntegerField(default=0)
    muda_status_paciente = models.IntegerField(default=0)

    cadastra_profissional = models.IntegerField(default=0)
    edita_profissional = models.IntegerField(default=0)
    acessa_cadastro_profissional = models.IntegerField(default=0)
    muda_status_profisisonal = models.IntegerField(default=0)

    observacoes = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=10, default='ATIVO')

    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, blank=True, null=False, on_delete=models.DO_NOTHING,)
    nome = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=True, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
    permissoes = models.ForeignKey(Permissoes, blank=True, null=False, on_delete=models.DO_NOTHING)
    model_template = models.CharField(max_length=100, blank=True, null=True)
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'usuarios'
        ordering = ('nome',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        senha = self.email.replace('.', '').replace('@', '')
        if not self.pk:
            user = User.objects.filter(username=self.email)
            if not user.count():
                user = User.objects.create_user(self.email, self.email, senha)
                user.save()
            self.usuario = user
        else:
            if not self.usuario:
                user = User.objects.filter(username=self.email)
                if not user.count():
                    user = User.objects.create_user(self.email, self.email, senha)
                    user.save()
                self.usuario = user
            else:
                self.usuario.username = self.email
                self.usuario.email = self.email
        super(Usuarios, self).save()
