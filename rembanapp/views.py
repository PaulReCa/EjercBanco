from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Usuario, Orden

# class Main(generic.View):
#     template_name='rembanapp/main.html'

def main(request):
  template = loader.get_template('rembanapp/main.html')
  return HttpResponse(template.render())


class IndexViewUsuarios(generic.ListView):
    template_name = 'rembanapp/indexUsuarios.html'
    context_object_name = 'listaUsuarios'

    def get_queryset(self):
        """Lista de Usuarios"""
        return Usuario.objects.all()

class IndexViewOrdenes(generic.ListView):
    template_name = 'rembanapp/indexOrdenes.html'
    context_object_name = 'listaOrdenes'

    def get_queryset(self):
        """Lista de Ordenes"""
        return Orden.objects.all()

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
    
class DetailViewOrdenes(generic.DetailView):
    model = Orden
    template_name = 'rembanapp/detailOrdenes.html'

    # Para que aparezca el link al Usuario de la Orden
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        orden = self.object
        usuarios = Usuario.objects.filter(orden=orden)
        context['usuarios'] = usuarios
        return context
