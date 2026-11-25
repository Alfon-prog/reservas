from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render



# Create your views here.
from django.http import Http404, HttpResponse
ESPACIOS = [
{"id": 1, "nombre": "Aula 12", "tipo": "aula", "aforo": 30},
{"id": 2, "nombre": "Laboratorio de Física", "tipo": "laboratorio",
"aforo": 24},
{"id": 3, "nombre": "Salón de actos", "tipo": "salon", "aforo": 200},
]
def buscar(pk): 
    for espacio in ESPACIOS:
        if espacio["id"] == pk: 
            return espacio
    raise Http404("El espacio no existe")

from django.shortcuts import get_object_or_404, render
from .models import Espacio

def lista(request):
 espacios = Espacio.objects.filter(activo=True)
 return render(request, "reservas/lista.html", {"espacios": ESPACIOS})

def detalle(request, pk):
 espacio = get_object_or_404(Espacio, pk=pk)
 return render(request, "reservas/detalle.html", {"espacio": buscar(pk)})


from django.utils import timezone
from django.views.generic import DetailView, ListView
from .models import Espacio, Reserva

class EspacioListView(ListView):
    template_name = "reservas/lista.html"

context_object_name = "espacios"
def get_queryset(self):
    return Espacio.objects.filter(activo=True)
class EspacioDetailView(DetailView):
    model = Espacio
template_name = "reservas/detalle.html"
context_object_name = "espacio"
def get_context_data(self, **kwargs):
    contexto = super().get_context_data(**kwargs)

    return contexto

