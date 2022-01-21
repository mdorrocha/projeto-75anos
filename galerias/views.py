import os
from django.shortcuts import render


def galeria(request, diretorio):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_galeria = 'galeria-' + diretorio
    try:
        galeria = os.listdir(os.path.join(base_dir, 'static/' + dir_galeria))
    except FileNotFoundError as ex:
        pass
    return render(request, 'galeria.html', {'galeria': sorted(galeria), 'diretorio': dir_galeria})
