from django.forms import ModelForm
from inscricoes.models import Inscricao


class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'email', 'telefone', 'cpf_rg','participa_almoco']
