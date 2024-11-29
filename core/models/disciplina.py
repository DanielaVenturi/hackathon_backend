from django.db import models
from .professor import Professor

class Disciplina(models.Model):
    disciplina_id = models.AutoField(primary_key=True)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True, default=None,)

class Meta:
    verbose_name_plural = "Disciplinas"
