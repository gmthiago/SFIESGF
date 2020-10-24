from django.contrib import admin
from cadastros.pacientes.models import Pacientes
from cadastros.profissional.models import Profissional
from cadastros.usuarios.models import Permissoes, Usuarios
from consultas.anamnese.models import Anamnese
from consultas.avaliacao.models import Avaliacao

admin.site.register(Usuarios)
admin.site.register(Permissoes)
admin.site.register(Pacientes)
admin.site.register(Profissional)
admin.site.register(Anamnese)
admin.site.register(Avaliacao)
