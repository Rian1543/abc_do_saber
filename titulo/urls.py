from django.urls import path
from titulo import views

urlpatterns = [
    
    #path('',views.inicio,name='index')
    path('',views.cadastrar,name='cadastrar_titulo'),
    path('listar/',views.listar,name='listar_titulo'),
]
