from django.shortcuts import render
from django.http import HttpResponse
from aluno.models import Aluno

# Create your views here.
def cadastrar(request):
    return render(request,'aluno/cadastroAluno.html')

def listar(request):
    registros=Aluno.objects.all()
        
    contexto={'aluno_lista':registros}
    
    return render(request,'aluno/listarAlunos.html',contexto)
