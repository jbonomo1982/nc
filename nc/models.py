from django.db import models
from django.utils import timezone



class accionInm(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    text = models.TextField(help_text=
    "Describir cómo se trato corregir la acción que genera la NC, en una prímera instancia")


class nC(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=200 ,help_text="Código propio del sistema.",blank=True,null=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechaApertura = models.DateTimeField(
            default=timezone.now)
    fechaSuceso = models.DateTimeField(
            blank=True, null=True)
    sector=None #Ver si se crea otra clase o se pone solo como opciones.

    accInm = models.ForeignKey(accionInm, on_delete=models.CASCADE)

    cerrada = models.BooleanField(default=False,help_text="Indica si la NC está cerrada.")
    
    
    

    def __str__(self):
        return '{0} {1}'.format(self.titulo,self.codigo)

class cierreNC(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nc = models.ForeignKey(nC, on_delete=models.CASCADE)
    fechaCierre = models.DateTimeField(
            default=timezone.now)
    observacion = models.TextField(help_text=
    "Informar sobre algo especial en el cierre de NC")

    def cerrar(self):
        #Configura los campos de la NC para el cierre de la misma:
        
        self.nc.cerrada = True
        self.save()






    