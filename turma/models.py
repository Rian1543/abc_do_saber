from django.db import models
from django.urls import reverse

# Create your models here.

class Turma(models.Model):
    
    numero=models.AutoField(primary_key=True,help_text='Numero')
    horariodaaula=models.TimeField(null=False,help_text='horario da aula')
    duracaodaaula=models.CharField(max_length=2,null=False,help_text='duracao da aula')
    datainicial=models.DateField(null=False,help_text='data inicial')
    datafinal=models.DateField(null=True,blank=True,help_text='data final')
    atividade=models.CharField(max_length=70,blank=True,null=False,help_text='atividade')
    instrutor=models.CharField(max_length=70,null=False,help_text='nome do instrutor')
    alunomonitor=models.CharField(max_length=70,null=False,help_text='aluno monitor')
    titularidade=models.CharField(max_length=70,null=False,help_text='titularidade do instrutor')
    
    def __str__(self):
        return f'{self.numero} - {self.horariodaaula} - {self.duracaodaaula} - {self.datainicial} -{self.datafinal} {self.atividade} - {self.instrutor} - {self.alunomonitor} - {self.titularidade}'