from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def programacao(request):
    return render(request, 'programacao.html')
