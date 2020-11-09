from agendamento.models import Agenda
from django import forms

class FormularioAgenda(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['nome', 'telefone', 'email', 'queixa']

