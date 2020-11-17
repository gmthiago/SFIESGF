from django.urls import path
from consultas.agenda.views import Agendas

urlpatterns = [
    path('agenda', Agendas, name='agenda'),
]