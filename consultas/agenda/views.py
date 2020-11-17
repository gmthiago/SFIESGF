from django.shortcuts import render
from django.views.generic import ListView
from consultas.agenda.forms import FormularioAgendamento
from consultas.agenda.models import Agenda

def Agendas (request):
    agenda = Agenda.objects.all()
    forms = FormularioAgendamento(request.POST or None)

    return render(request, 'initial_page.html', {'agenda': agenda, 'forms': forms})