from django.urls import path
from galerias import views

urlpatterns = [
    path('<diretorio>', views.galeria, name='galeria'),
]