from django.shortcuts import render
from django.http import HttpResponse
from instrutor.models import Instrutor

# Create your views here.
def cadastrar(request):
    return render(request,'instrutor/cadastroInstrutor.html')

def listar(request):
    registros=Instrutor.objects.all()   

    contexto={'instrutor_lista':registros}
    
    return render(request,'instrutor/listarInstrutores.html',contexto)