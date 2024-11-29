from django.db import models
from .disciplina import Disciplina
from .turma import Turma


class TurmaHasDisciplina(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
