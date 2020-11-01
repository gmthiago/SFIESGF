from cadastros.pacientes.models import Pacientes
from django import forms


class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nome_paciente', 'profissional', 'data_nascimento', 'status', 'email']