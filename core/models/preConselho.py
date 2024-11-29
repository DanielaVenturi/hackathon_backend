from django.db import models
from .turma import Turma
from .trimestre import Trimestre

class PreConselho(models.Model):
    preConselho_id = models.AutoField(primary_key=True)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True, default=None,)
    trimestre = models.ForeignKey(Trimestre, on_delete=models.SET_NULL, null=True, blank=True, default=None,)