from hashlib import sha256
import os
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
# def cadastro (request):
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             return redirect('/')
#         return render(request, 'cadastro.html')
#     elif request.method == 'POST':
#         usuario = request.POST.get('usuario')
#         email = request.POST.get('email')
#         senha = request.POST.get('senha')
#         confirmar_senha = request.POST.get('confirmar_senha')
#
#         if not password_is_valid(request, senha, confirmar_senha):
#             return redirect('/auth/cadastro')
#         try:
#             user = User.objects.create_user(username=usuario,
#                                             email=email,
#                                             password=senha,
#                                             is_active=False)
#             user.save()
#
#             token = sha256(f"{usuario}{email}".encode()).hexdigest()
#             ativacao = Ativacao(token=token, user=user)
#             ativacao.save()
#
#             path_template = os.path.join(settings.BASE_DIR, 'autenticacao/templates/emails/cadastro_confirmado.html')
#             email_html(path_template, 'Cadastro confirmado', [email,], username=usuario, link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")
#
#             messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
#             return redirect('/auth/logar')
#         except:
#             messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
#             return redirect('/auth/cadastro')

def cadastro (request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        form = FuncionarioForm()
        return render(request, 'cadastrar_funcionario.html', {'form':form})
    elif request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()

            lista_itens = Funcionario.objects.order_by('-funcRegistro')[0]
            usuario = lista_itens.funcNome
            e_mail = lista_itens.funcEmail
            passwd = lista_itens.funcSenha
            confirm_passwd = lista_itens.funcConfirmarSenha
            cadastro = lista_itens.funcTipoCadastro

            if not password_is_valid(request, passwd, confirm_passwd):
                return redirect('/auth/cadastro')
            try:
                user = User.objects.create_user(username=usuario,
                                                email=e_mail,
                                                password=passwd,
                                                is_active=False)
                user.save()

                token = sha256(f"{usuario}{e_mail}".encode()).hexdigest()
                ativacao = Ativacao(token=token, user=user)
                ativacao.save()

                path_template = os.path.join(settings.BASE_DIR, 'autenticacao/templates/emails/cadastro_confirmado.html')
                email_html(path_template, 'Cadastro confirmado', [e_mail,], username=usuario, link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")

                messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
                return redirect('/auth/logar')
            except:
                messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
                return redirect('/auth/cadastro')
