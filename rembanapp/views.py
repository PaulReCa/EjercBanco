from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Usuario, Orden


class IndexView(generic.ListView):
    template_name = 'rembanapp/index.html'
    context_object_name = 'listaUsuarios'

    def get_queryset(self):
        """Lista de Usuarios"""
        return Usuario.objects.all()
    
class DetailView(generic.DetailView):
    model = Usuario
    template_name = 'rembanapp/detail.html'
