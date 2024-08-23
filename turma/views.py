from django.shortcuts import render
from django.http import HttpResponse
from turma.models import Turma


# Create your views here.
def cadastrar(request):
    return render(request,'turma/cadastroTurma.html')

def listar(request):
     registros=Turma.objects.all()
        
     contexto={'turma_lista':registros}
     return render(request,'turma/listarTurmas.html',contexto)

def construcao(request):
     return render(request,'turma/paginaemconstrucao.html')

def registro(request):
     return render(request,'turma/registroAusencia.html')