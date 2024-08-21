from django.db import models
from django.urls import reverse

# Create your models here.

class TipoAtividade(models.Model):
    
    codigo=models.IntegerField(primary_key=True,help_text='Codigo do tipo de atividade')
    descricao=models.CharField(max_length=70,null=False,help_text='Informe a descricao do tipo de atividade')
    
    def __str__(self):
        return f'{self.codigo} {self.descricao}'
    