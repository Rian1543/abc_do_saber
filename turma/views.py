from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request,'turma/cadastroTurma.html')

def listar(request):
     return render(request,'turma/listarTurmas.html')

def construcao(request):
     return render(request,'turma/paginaemconstrucao.html')

def registro(request):
     return render(request,'turma/registroAusencia.html')