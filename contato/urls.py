from django.urls import path
from contato import views

urlpatterns = [
    
    #path('',views.inicio,name='index')
    path('',views.registrar_contato,name='registrar_contato'),
]
