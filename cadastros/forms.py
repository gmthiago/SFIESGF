from cadastros.pacientes.models import Pacientes
from django import forms
from cadastros.usuarios.models import Usuarios


class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nome_paciente', 'profissional', 'data_nascimento', 'status', 'email']

