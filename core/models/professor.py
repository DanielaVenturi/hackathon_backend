from django.db import models

class Professor(models.Model):
    professor_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    email = models.EmailField(max_length=255)
    nome = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Professores"