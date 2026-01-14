from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    titulo:models.CharField = models.CharField(max_length=200)
    descripcion:models.TextField = models.TextField(blank=True)

    fecha_creacion:models.DateTimeField = models.DateTimeField(auto_now_add=True)
    fecha_limite:models.DateField = models.DateField()

    propietario:models.ForeignKey = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name="proyectos_propietarios")
    
    colaboradores:models.ManyToManyField = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return self.titulo
    
class Tarea(models.Model):
    ESTADO = [("TODO", "Pendiente"),("INPROG", "En progreso"),("DONE", "Completada")]
    PRIORIDAD = [("L","Baja"),("M","Media"),("H","Alta")]

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="tareas")
    titulo = models.CharField(max_length=200)
    estado = models.CharField(max_length=6, choices=ESTADO, default="TODO")
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD, default="M")
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f"{self.titulo} ({self.proyecto.titulo})"