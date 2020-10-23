from django.contrib.auth.models import User
from django.db import models

class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, blank=True, null=True, on_delete=models.DO_NOTHING,)
    nome = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, null=True, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
    ))
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
