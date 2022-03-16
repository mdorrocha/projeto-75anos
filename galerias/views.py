import os
from aniversario_campus_pelotas import settings
from django.shortcuts import render


def galeria(request, diretorio):
    dir_galeria = 'galeria-' + diretorio
    try:
        galeria = os.listdir(os.path.join(settings.STATIC_ROOT, dir_galeria))
    except FileNotFoundError as ex:
        pass
    return render(request, 'galeria.html', {'galeria': sorted(galeria), 'diretorio': dir_galeria})
