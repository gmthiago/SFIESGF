from django.shortcuts import render
from .forms import FormularioPaciente
from cadastros.pacientes.models import Pacientes
from cadastros.usuarios.models import Usuarios


def TelaPaciente(request):
    pacientes = Pacientes.objects.all()
    forms = FormularioPaciente(request.POST or None)

    if forms.is_valid():
        cadastrado = forms.save(commit=False)
        cadastrado.save()
        return render(request, 'index.html', {'pacientes': pacientes, 'forms': forms})

    return render(request, 'index.html', {'pacientes': pacientes, 'forms': forms})



