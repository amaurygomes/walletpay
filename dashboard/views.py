from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from efipay import EfiPay
from efi.credentials import credentials
from .models import API
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django import forms



efi = EfiPay(credentials.CREDENTIALS)


@login_required
def index(request):

    response = efi.get_account_balance()
    saldo = response.get('saldo')

    contexto = {
        'saldo': saldo
    }


    return render(request, 'dashboard/index.html', contexto)


@login_required
def solicitacoes(request):
    response =  efi.pix_list_evp()
    print(response)

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

@login_required
def password(request):
    contexto = {
        
    }

    return render(request, 'dashboard/change_password.html', contexto)


@login_required
def config(request):
    
    
    api = API.objects.get(pk=1)
    contexto = {
        'api': api
    }

    return render(request, 'dashboard/config.html', contexto)  # Substitua 'seu_template.html' pelo seu template HTML



class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Senha Antiga', widget=forms.PasswordInput)
    new_password = forms.CharField(label='Nova Senha', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirmar Nova Senha', widget=forms.PasswordInput)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']
            
            if request.user.check_password(old_password) and new_password == confirm_new_password:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Sua senha foi alterada com sucesso!')
                return redirect('change_password')
            else:
                messages.error(request, 'Houve um erro ao alterar sua senha. Certifique-se de digitar corretamente a senha antiga e a nova senha.')
    else:
        form = ChangePasswordForm()
    
    return render(request, 'dashboard/change_password.html', {'form': form})