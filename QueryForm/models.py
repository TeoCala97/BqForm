from tabnanny import verbose
from django.db import models

# Create your models here.
class Form(models.Model):

    LISTA = [("",""),
            ("S1","Seleccion 1"),
            ("S2","Seleccion 2"),
            ("S3","Seleccion 3"),
            ("S4","Seleccion 4"),
            ("S5","Seleccion 5"),]

    qname = models.CharField(max_length=200, verbose_name="Nombre")
    select =  models.CharField(max_length=10,choices=LISTA,verbose_name="Desplegables")
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True ,verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True ,verbose_name="fecha de edición")

    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"
        ordering = ["-created"]
    
    def __str__(self):
        return self.qname
