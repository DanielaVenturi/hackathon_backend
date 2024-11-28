from django.db import models

class Turma(models.Model):
    turma_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)