from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse ('<html><body><h2>pagina escola<\h2><p>Olá,esta é a pagina escola</p></body></html>')
