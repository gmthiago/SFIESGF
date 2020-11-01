from django.shortcuts import render
from cadastros.forms import FormularioPaciente


def TelaPaciente(request):
    pacientes = FormularioPaciente.objects.all()

    return render(request, 'index.html', {'pacientes': pacientes})

