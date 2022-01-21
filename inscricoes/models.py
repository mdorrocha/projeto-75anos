# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Inscricao(models.Model):
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    nome = models.CharField(max_length=200, verbose_name='Nome')
    dt_inscricao = models.DateTimeField(verbose_name='Data da Inscrição', auto_now_add=timezone.now)
    email = models.EmailField(max_length=60)
    telefone = models.CharField(max_length=40)
    cpf_rg = models.CharField(max_length=40, verbose_name='CPF ou RG')
    participa_almoco = models.BooleanField(default=False, verbose_name='Participará do Almoço de Confraternização')

    def __str__(self):
        return self.nome
