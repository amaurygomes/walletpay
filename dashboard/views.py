from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    contexto = {
        
    }


    return render(request, 'dashboard/index.html', contexto)


@login_required
def solicitacoes(request):
    contexto = {
        
    }

    return render(request, 'dashboard/solicitacoes.html', contexto)


@login_required
def pagamentos(request):
    contexto = {
        
    }

    return render(request, 'dashboard/pagamentos.html', contexto)


@login_required
def relatorios(request):
    contexto = {
        
    }

    return render(request, 'dashboard/relatorios.html', contexto)