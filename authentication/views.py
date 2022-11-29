from datetime import date
from hashlib import sha256
import os
import re
from validate_docbr import CPF, CNPJ
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from authentication.forms import FuncionarioForm
from authentication.models import Ativacao
from authentication.utils import password_is_valid, email_html
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
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
        cpf = CPF()
        if form.is_valid():
            item = form.save(commit=False)

            item_funcNome = form.cleaned_data['funcNome']
            item_funcEmail = form.cleaned_data['funcEmail']
            item_funcTipoCadastro = form.cleaned_data['funcTipoCadastro']
            item_funcCpf = form.cleaned_data['funcCpf']

            today = date.today()
            data = today.strftime("%Y")

            item_funcSenha = (f"Fatec_ads@{data}")
            item_funcConfirmarSenha = item_funcSenha

            usuario = item_funcEmail
            e_mail = item_funcEmail
            passwd = item_funcSenha
            confirm_passwd = item_funcConfirmarSenha
            cadastro = item_funcTipoCadastro

            if not password_is_valid(request, passwd, confirm_passwd):
                item = get_object_or_404(Funcionario, pk=item.funcRegistro)
                item.delete()
                return render(request, 'cadastro.html', {'form': form})
            
            # #formatacao
            # if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', item_funcCpf):
            #     messages.add_message(request, constants.ERROR, 'CPF inválido')
            #     return render(request, 'cadastro.html', {'form': form})
            
            # #quantidade de digitos
            # numbers = [int(digit) for digit in item_funcCpf if digit.isdigit()]

            # #verifica a quantidade
            # if len(numbers) != 11 or len(set(numbers)) == 1:
            #     messages.add_message(request, constants.ERROR, 'CPF inválido')
            #     return render(request, 'cadastro.html', {'form': form})
            
            # #calculo para primeiro digito
            # sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
            # expected_digit = (sum_of_products * 10 % 11) % 10
            # if numbers[9] != expected_digit:
            #     messages.add_message(request, constants.ERROR, 'CPF inválido')
            #     return render(request, 'cadastro.html', {'form': form})
            
            # #calculo para segundo digito
            # sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
            # expected_digit = (sum_of_products * 10 % 11) % 10
            # if numbers[10] != expected_digit:
            #     messages.add_message(request, constants.ERROR, 'CPF inválido')
            #     return render(request, 'cadastro.html', {'form': form})

            if not cpf.validate(item_funcCpf):
                messages.add_message(request, constants.ERROR, 'CPF inválido')
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

                    link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}"

                    html_content = render_to_string('emails/cadastro_confirmado.html', {'username': usuario, 'password': passwd, 'link_ativacao': link_ativacao})
                    text_content = strip_tags(html_content)

                    email = EmailMultiAlternatives('Cadastro Confirmado!', text_content, settings.EMAIL_HOST_USER, [e_mail])
                    email.attach_alternative(html_content, 'text/html')

                    email.send()
                    return render(request, 'salvo.html', {})

                except:
                    messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
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

                    link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}"

                    html_content = render_to_string('emails/cadastro_confirmado.html', {'username': usuario, 'password': passwd, 'link_ativacao': link_ativacao})
                    text_content = strip_tags(html_content)

                    email = EmailMultiAlternatives('Cadastro Confirmado!', text_content, settings.EMAIL_HOST_USER, [e_mail])
                    email.attach_alternative(html_content, 'text/html')

                    email.send()
                                        
                    return render(request, 'salvo.html', {})

                except:
                    messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
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
                    messages.add_message(request, constants.ERROR, 'Você precisa trocar sua senha')
                    return redirect('/auth/alterar_senha')
                else:
                    return redirect('/index/')
            elif password == item_funcSenha:
                    messages.add_message(request, constants.ERROR, 'Você precisa trocar sua senha')
                    return redirect('/auth/alterar_senha')
            else:
                usuario
                messages.add_message(request, constants.ERROR, 'Você nao tem permissao')
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
    messages.add_message(request, constants.SUCCESS, 'Conta ativada com sucesso!!!')

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
            messages.add_message(request, constants.SUCCESS, 'Senha cadastrada com sucesso!')
            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
            return redirect('/auth/alterar_senha')

    return render(request, 'alterar_senha.html')
