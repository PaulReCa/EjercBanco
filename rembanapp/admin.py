from django.contrib import admin
from .models import Usuario
from .models import Orden

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
  list_display = ("Nombre", "Apellidos", "Email", "Telefono","id",)
admin.site.register(Usuario, UsuarioAdmin)

class OrdenAdmin(admin.ModelAdmin):
  list_display = ("Cantidad", "NumCuenta", "Beneficiario", "Banco","id",)
admin.site.register(Orden, OrdenAdmin)