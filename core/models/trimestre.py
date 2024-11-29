from django.db import models


class Trimestre(models.Model):
    trimestre_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)  
    data_inicio = models.DateField()  
    data_fim = models.DateField() 
    def _str_(self):
        return self.nome
