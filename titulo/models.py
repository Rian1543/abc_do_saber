from django.db import models
from django.urls import reverse

# Create your models here.

class Titulo(models.Model):
    
    codigo=models.AutoField(primary_key=True,help_text='Codigo do titulo')
    descricao=models.CharField(max_length=70,null=False,help_text='Informe a descricao do titulo')
    
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'