from django.urls import path
from tipoAtividade import views

urlpatterns = [
    
    path('',views.inicio,name='index')
]
