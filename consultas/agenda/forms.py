from consultas.agenda.models import Agenda
from django import forms

class FormularioAgendamento(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['paciente', 'alunoa', 'alunob', 'data_agendamento']