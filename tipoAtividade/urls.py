from django.urls import path
from tipoAtividade import views

urlpatterns = [
    
    #path('',views.inicio,name='index')
    path('',views.cadastrar,name='cadastrar'),
    path('listar/',views.listar,name='listar')
]
