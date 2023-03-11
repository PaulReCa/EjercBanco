from django.db import models

class Usuario(models.Model):
  Nombre = models.CharField(max_length=50, blank=False, null=False)
  Apellidos = models.CharField(max_length=100, blank=False, null=False)
  Email = models.EmailField(max_length=100, blank=False, null=False)
  Telefono = models.PositiveIntegerField(blank=False, null=False)

  def __str__(self):
    return f"{self.Nombre} {self.Apellidos}"
  
class Orden(models.Model):

  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)

  Cantidad = models.FloatField(blank=False, null=False)
  NumCuenta = models.CharField(max_length=50, blank=False, null=False)
  Beneficiario = models.CharField(max_length=100, blank=False, null=False)
  Concepto = models.TextField(max_length=200, blank=False, null=False)
  Banco = models.CharField(max_length=50, blank=False, null=False)

  def __str__(self):
    return f"{self.Cantidad}€ para {self.Beneficiario}"
