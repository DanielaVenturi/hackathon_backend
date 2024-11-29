from django.db import models
from .user import User
from .aluno import Aluno


class Ocorrencia(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria_ocorrencia = models.CharField(max_length=100)
    data_criacao = models.DateField()

class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"