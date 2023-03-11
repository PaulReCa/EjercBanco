from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Usuario, Orden


class IndexViewUsuarios(generic.ListView):
    template_name = 'rembanapp/indexUsuarios.html'
    context_object_name = 'listaUsuarios'

    def get_queryset(self):
        """Lista de Usuarios"""
        return Usuario.objects.all()
    
class DetailViewUsuarios(generic.DetailView):
    model = Usuario
    template_name = 'rembanapp/detailUsuarios.html'

    # Para que aparezca debajo las Ordenes de ese Usuario
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        usuario = self.object
        ordenes = Orden.objects.filter(usuario=usuario)
        context['ordenes'] = ordenes
        return context