from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return "Tarefa: " + self.task + " Detalhes: " + self.description