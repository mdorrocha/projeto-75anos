from django.db import transaction
from django.shortcuts import render
from inscricoes import utils
from inscricoes.forms import InscricaoForm
from inscricoes.models import Inscricao
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse


@transaction.atomic
def adicionar_inscricao(request):
    if request.method == "GET":
        form = InscricaoForm()
    else:
        form = InscricaoForm(request.POST)
        if form.is_valid():
            inscricao = Inscricao()
            inscricao.nome = request.POST.get('nome')
            inscricao.email = request.POST.get('email')
            inscricao.telefone = request.POST.get('telefone')
            inscricao.cpf_rg = request.POST.get('cpf_rg')
            inscricao.participa_almoco = bool(request.POST.get('participa_almoco'))
            inscricao.save()
            messages.add_message(request, messages.SUCCESS, 'Sua inscrição foi realizada com sucesso! '
                                                            'Você receberá um e-mail com instruções. '
                                                            'Se não encontrar o e-mail, verifique a sua caixa de SPAM '
                                                            'ou a lixeira do seu gerenciador de e-mails.')
    return render(request, 'form_inscricao_add.html', {'form': form})


@login_required
def exportar_inscricoes(request):
    fields = ["id", "nome", "email", "telefone", "cpf_rg", "participa_almoco"]
    queryset = Inscricao.objects.all().order_by('nome')
    try:
        book, nome_arquivo = utils.export_xlwt(Inscricao, queryset.values_list(*fields), fields)
    except Exception:
        raise

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % nome_arquivo
    book.save(response)
    return response
