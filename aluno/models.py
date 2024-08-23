from django.db import models
from django.urls import reverse

# Create your models here.

class Aluno(models.Model):
    
    matricula=models.AutoField(primary_key=True,help_text='matricula do aluno')
    nome=models.CharField(max_length=70,null=False,help_text='nome do aluno')
    datainicial=models.DateField(null=False,help_text='data inicial')
    datafinal=models.DateField(null=True,blank=True,help_text='data final')
    
    
    def __str__(self):
        return f'{self.matricula} - {self.nome} - {self.datainicial} - {self.datafinal}'