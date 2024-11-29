from django.db import models
from .turma import Turma

class Aluno(models.Model):
    pkAluno = models.CharField(max_length=45, primary_key=True)
    email = models.EmailField(max_length=255)
    nomeAluno = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE)
