from django.db import models
from .trimestre import Trimestre
from .aluno import Aluno


class ConselhoClasse(models.Model):
    class StatusChoices(models.TextChoices):
        PENDENTE = 'Pendente', 'Pendente'
        EM_ANDAMENTO = 'Em andamento', 'Em andamento'
        FINALIZADO = 'Finalizado', 'Finalizado'

    conselho_id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_conselho = models.DateField()
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDENTE
    )

    def __str__(self):
        return f"Conselho {self.conselho_id} - {self.status}"
    
    class Meta:
        verbose_name_plural = "Conselhos de Classe"
