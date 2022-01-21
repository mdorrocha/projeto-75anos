from django.urls import path
from inscricoes import views

urlpatterns = [
    path('add', views.adicionar_inscricao, name='inscricao_add'),
]