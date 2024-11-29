from django.db import models
from .disciplina import Disciplina
from .aluno import Aluno
from .conselhoClasse import ConselhoClasse

class Nota(models.Model):
    nota_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    conselho = models.ForeignKey(ConselhoClasse, on_delete=models.CASCADE)
    trimestre = models.CharField(max_length=20, choices=[('1', 'Primeiro'), ('2', 'Segundo'), ('3', 'Terceiro')])
    valor = models.DecimalField(max_digits=5, decimal_places=2)
