from django.contrib import admin
from cadastros.usuarios.models import Usuarios, Permissoes

admin.site.register(Usuarios)
admin.site.register(Permissoes)
