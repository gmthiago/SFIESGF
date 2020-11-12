from django.urls import path
from agendamento.views import Agendamento

urlpatterns = [
    path('agenda', Agendamento, name='agendamento'),
]

