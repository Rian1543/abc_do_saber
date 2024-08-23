from django.db import models
from django.urls import reverse

# Create your models here.

class Instrutor(models.Model):
    
    id=models.AutoField(primary_key=True,help_text='id do instrutor')
    nome=models.CharField(max_length=70,null=False,help_text='nome do instrutor')
    rg=models.CharField(max_length=9,null=False,help_text='rg do instrutor')
    datadenascimento=models.DateField(null=False,help_text='data de nascimento')
    ddd=models.CharField(max_length=3,null=False,blank=True,help_text='ddd do intrutor')
    telefone=models.CharField(max_length=9,null=False,blank=True,help_text='telefone do intrutor')
    titularidade=models.CharField(max_length=70,null=False,help_text='titularidade do instrutor')
    
    def __str__(self):
        return f'{self.id} - {self.nome} - {self.rg} - {self.datadenascimento} -{self.ddd} - {self.telefone} - {self.titularidade}'