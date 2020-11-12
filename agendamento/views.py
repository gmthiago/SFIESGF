from django.shortcuts import render, redirect
from django.http import HttpResponse
from agendamento.forms import FormularioAgenda
from agendamento.models import Agenda


def Agendamento(request):
    agenda = Agenda.objects.all()
    forms = FormularioAgenda(request.POST or None)

    if forms.is_valid():
        agendado = forms.save(commit=False)
        agendado.save()
        return render(request, 'agenda.html', {'agenda': agenda, 'forms': forms})

    return render(request, 'agenda.html', {'agenda': agenda, 'forms': forms})



