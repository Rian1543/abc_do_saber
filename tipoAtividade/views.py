from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse ('<html><body><h2>Pagina Tipo Atividades</h2><p>Olá, esta é a página tipos atividades</p></body></html>')

def cadastrar(request):
    return render(request,'tipoAtividade/cadastroTiposAtividade.html')

def listar(request):
     return render(request,'tipoAtividade/listarTiposAtividade.html')