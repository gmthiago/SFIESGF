from django.shortcuts import render, redirect
from consultas.agenda.models import Agenda
from consultas.agenda.forms import FormularioAgendamento


def Agendas(request):
    agenda = Agenda.objects.all()
    forms = FormularioAgendamento(request.POST or None)

    return render(request, 'initial_page.html', {'agenda': agenda, 'forms': forms})
