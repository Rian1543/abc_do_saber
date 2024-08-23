from django.shortcuts import render
from django.http import HttpResponse
from titulo.models import Titulo

# Create your views here.
def cadastrar(request):
    return render(request,'titulo/cadastroTitulos.html')

def listar(request):
    
    registros=Titulo.objects.all()
    
    contexto={'titulo_lista':registros}
    
    return render(request,'titulo/listarTitulos.html',contexto)