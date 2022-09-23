from datetime import date
from hashlib import sha256
import os
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from authentication.forms import FuncionarioForm
from authentication.models import Ativacao
from authentication.utils import password_is_valid, email_html
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.conf import settings
from easyreport_web.models import Funcionario


# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('/')
        form = FuncionarioForm()
        return render(request, 'cadastro.html', {'form': form})
    elif request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)

            item_funcNome = form.cleaned_data['funcNome']
            item_funcEmail = form.cleaned_data['funcEmail']
            item_funcTipoCadastro = form.cleaned_data['funcTipoCadastro']

            today = date.today()
            data = today.strftime("%Y")

            item_funcSenha = (f"Fatec_ads@{data}")
            item_funcConfirmarSenha = item_funcSenha

            usuario = item_funcNome
            e_mail = item_funcEmail
            passwd = item_funcSenha
            confirm_passwd = item_funcConfirmarSenha
            cadastro = item_funcTipoCadastro

            if not password_is_valid(request, passwd, confirm_passwd):
                item = get_object_or_404(Funcionario, pk=item.funcRegistro)
                item.delete()
                return render(request, 'cadastro.html', {'form': form})

            if cadastro == 'Funcionario':
                try:
                    user = User.objects.create_user(username=usuario,
                                                    email=e_mail,
                                                    password=passwd,
                                                    is_active=False)
                    user.save()
                    form.save()


                    token = sha256(f"{usuario}{e_mail}".encode()).hexdigest()
                    ativacao = Ativacao(token=token, user=user)
                    ativacao.save()

                    path_template = os.path.join(settings.BASE_DIR,
                                                 'authentication/templates/emails/cadastro_confirmado.html')
                    email_html(path_template, 'Cadastro confirmado', [e_mail, ], username=usuario, password=passwd,
                               link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")

                    messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')

                    return redirect('/index/')
                except:
                    messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
                    return render(request, 'cadastro.html', {'form': form})
            else:
                try:
                    user = User.objects.create_superuser(username=usuario,
                                                    email=e_mail,
                                                    password=passwd,
                                                    is_active=False)
                    user.save()
                    form.save()

                    token = sha256(f"{usuario}{e_mail}".encode()).hexdigest()
                    ativacao = Ativacao(token=token, user=user)
                    ativacao.save()

                    path_template = os.path.join(settings.BASE_DIR,
                                                 'authentication/templates/emails/cadastro_confirmado.html')
                    email_html(path_template, 'Cadastro confirmado', [e_mail, ], username=usuario, password=passwd,
                               link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")

                    messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
                    return redirect('/index/')
                except:
                    messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
                    return render(request, 'cadastro.html', {'form': form})

    else:
        form = FuncionarioForm()

    return render(request, 'cadastro.html', {'form': form})

def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')

def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=password)

        today = date.today()
        data = today.strftime("%Y")

        item_funcSenha = (f"Fatec_ads@{data}")

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/auth/logar')

        elif usuario is not None:
            login(request, usuario)
            if usuario.has_perm('does.not.exist'):
                if password == item_funcSenha:
                    messages.add_message(request, constants.ERROR, 'Voce precisa trocar sua senha')
                    return redirect('/auth/alterar_senha')
                else:
                    return redirect('/index/')
            else:
                usuario
                messages.add_message(request, constants.ERROR, 'Voce nao tem permissao')
                logout(request)
                return redirect('/auth/logar')

def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Essa token já foi usado')
        return redirect('/auth/logar')

    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()
    messages.add_message(request, constants.SUCCESS, 'Conta ativa com sucesso')

    return redirect('/auth/logar')

def alterar_senha(request):
    if request.method == "POST":
        usuario = request.user
        password = request.POST.get('password')
        confirm_passwd = request.POST.get('confirm_password')

        if not password_is_valid(request, password, confirm_passwd):
            return render(request, 'alterar_senha.html')

        try:
            usuario.set_password(password)
            usuario.save()
            logout(request)
            messages.add_message(request, constants.SUCCESS, 'Senha cadastrada com sucesso')
            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
            return redirect('/auth/alterar_senha')

    return render(request, 'alterar_senha.html')
