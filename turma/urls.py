from django.urls import path
from turma import views

urlpatterns = [
    
    #path('',views.inicio,name='index')
    path('',views.cadastrar,name='cadastrar_turma'),
    path('listar/',views.listar,name='listar_turma'),
    path('construcao/',views.construcao,name='pagina_em_construcao'),
    path('registro/',views.registro,name='registro_ausencia'),
]
