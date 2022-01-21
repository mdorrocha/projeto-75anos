from django.urls import path
from principal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programacao', views.programacao, name='programacao'),
]
