from django.views.generic import ListView
from consultas.agenda.models import Agenda

class Agendas(ListView):
    template_name = "initial_page.html"
    model = Agenda
    context_object_name = "agendamentos"