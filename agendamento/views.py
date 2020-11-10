from django.shortcuts import render
from django.http import HttpResponse
from agendamento.forms import FormularioAgenda

def Agendamento(request):
    agenda = Agendamento.objects.all()
    forms = FormularioAgenda(request.POST or None)
    return (request, 'agenda.html')

    if forms.is_valid():
        agendado = forms.save(commit=False)
        agendado.save()
        return render(request, 'agenda.html', {'agenda': agenda, 'forms': forms})



