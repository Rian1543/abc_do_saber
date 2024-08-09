from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
        return HttpResponse ('<html><body><h2>Pagina Escola</h2><p>Olá, esta é a página escola</p></body></html>')

def escola(request):
        return render(request, 'escola.html')