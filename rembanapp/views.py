from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# from audioop import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Usuario, Orden

# class Main(generic.View):
#     template_name='rembanapp/main.html'

def main(request):
  template = loader.get_template('rembanapp/main.html')
  return HttpResponse(template.render())

# -----------------------------------------------------------

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
    
# -----------------------------------------------------------

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

# -----------------------------------------------------------

class UsuarioCreateView(CreateView):
    model = Usuario
    fields = '__all__'
    # success_url='/rembanapp/indexUsuarios/'  
    def get_success_url(self):
        return reverse('rembanapp:detailUsuarios', kwargs={'pk': self.object.id})

class OrdenCreateView(CreateView):
    model = Orden
    fields = '__all__'
    # success_url='/rembanapp/indexOrdenes/'  
    def get_success_url(self):
        return reverse('rembanapp:detailOrdenes', kwargs={'pk': self.object.id})

# -----------------------------------------------------------

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = '/rembanapp/indexUsuarios/'  # *? hacer con get_absolute_url del modelo
    # success_url = reverse_lazy('/rembanapp/indexUsuarios/')

class OrdenDeleteView(DeleteView):
    model = Orden
    success_url = '/rembanapp/indexOrdenes/'  # *? hacer con get_absolute_url del modelo
    # success_url = reverse_lazy('/rembanapp/indexOrdenes/')

# -----------------------------------------------------------

class UsuarioUpdateView(UpdateView):
    model = Usuario
    fields = '__all__'
    template_name_suffix = '_update_form'
    # success_url = '/rembanapp/indexUsuarios/'

    def get_success_url(self):
        return reverse('rembanapp:detailUsuarios', kwargs={'pk': self.object.id})

    # success_url = reverse_lazy('rembanapp:detailUsuarios', kwargs={'pk': self.object.id})

class OrdenUpdateView(UpdateView):
    model = Orden
    fields = '__all__'
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('rembanapp:detailOrdenes', kwargs={'pk': self.object.id})

