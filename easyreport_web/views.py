from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from easyreport_web.models import *
from easyreport_web.forms import *
import requests

mainUrl = ('http://127.0.0.1:8080/')

# Create your views here.
def splash(request):
    return render(request, 'splash.html')

def index(request):
    return render(request,'index.html')

#USER LOGIN
def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            if usuario.has_perm('does.not.exist'):
                return redirect('/index/')
            else:
                usuario
                messages.error(request, 'Você não tem permissão')
                logout(request)
        else:
            messages.error(request, 'Usuário ou senha inválido')

    return redirect('/login/')

#USER LOGOUT
def logout_user(request):
    logout(request)
    return redirect('/')

#FUNCIONARIO
def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()

            lista_itens = Funcionario.objects.order_by('-funcRegistro')[0]
            usuario = lista_itens.funcNome            
            e_mail = lista_itens.funcEmail
            passwd = lista_itens.funcSenha
            cadastro = lista_itens.funcTipoCadastro    
            
            if cadastro == 'Funcionario':
                User.objects.create_user(
                    username=str(usuario), email = str(e_mail), password = str(passwd)
                )
            else:
                User.objects.create_superuser(
                    username=str(usuario), email = str(e_mail), password = str(passwd)
                )
                
            return render(request, 'salvo.html', {})
    
    else:
        form = FuncionarioForm()
    
    return render(request, 'cadastrar_funcionario.html', {'form':form})

def listar_funcionario(request):
    lista_itens = Funcionario.objects.all()
    return render(request, 'listar_funcionario.html', {'lista_itens': lista_itens})

def funcionario(request, nr_item):
    funcionario = get_object_or_404(Funcionario, pk=nr_item)
    return render(request, 'funcionario.html', {'item': funcionario})

def editar_funcionario(request, nr_item):    
    item = get_object_or_404(Funcionario, pk=nr_item)
    form = FuncionarioForm(instance=item)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.funcCpf = form.cleaned_data['funcCpf']
            item.funcNome = form.cleaned_data['funcNome']
            item.funcEnderecoRua = form.cleaned_data['funcEnderecoRua']
            item.funcEnderecoNumero = form.cleaned_data['funcEnderecoNumero']
            item.funcEnderecoComplemento = form.cleaned_data['funcEnderecoComplemento']
            item.funcEnderecoCidade = form.cleaned_data['funcEnderecoCidade']
            item.funcEnderecoCep = form.cleaned_data['funcEnderecoCep']
            item.funcTelefone = form.cleaned_data['funcTelefone']
            item.funcEmail = form.cleaned_data['funcEmail']
            item.funcSenha = form.cleaned_data['funcSenha']
            item.funcFuncao = form.cleaned_data['funcFuncao']
            item.funcDpto = form.cleaned_data['funcDpto']
            item.funcCnh = form.cleaned_data['funcCnh']
            item.funcEnderecoEstado = form.cleaned_data['funcEnderecoEstado']
            item.funcTipoCadastro = form.cleaned_data['funcTipoCadastro']

            item.save()

            return render(request, 'atualizado.html', {})
        
        else:
            return render(request, 'cadastrar_funcionario.html', {'form':form, 'item': item})
    
    elif (request.method == 'GET'):
        return render(request, 'editar_funcionario.html', {'form':form, 'item': item})

def excluir_funcionario(request, nr_item):
    item = get_object_or_404(Funcionario, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

#VEICULO
def cadastrar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo.html', {})
    
    else:
        form = VeiculoForm()
    
    return render(request, 'cadastrar_veiculo.html', {'form':form})

def listar_veiculo(request):
    lista_itens = Veiculo.objects.all()
    return render(request, 'listar_veiculo.html', {'lista_itens': lista_itens})

def veiculo(request, nr_item):
    veiculo = get_object_or_404(Veiculo, pk=nr_item)
    return render(request, 'veiculo.html', {'item': veiculo})

def editar_veiculo(request, nr_item):    
    item = get_object_or_404(Veiculo, pk=nr_item)
    form = VeiculoForm(instance=item)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.veicPlaca = form.cleaned_data['veicPlaca']
            item.veicModelo = form.cleaned_data['veicModelo']
            item.veicFabricante = form.cleaned_data['veicFabricante']
            item.veicAno = form.cleaned_data['veicAno']
            item.veicCor = form.cleaned_data['veicCor']
            item.veicRenavam = form.cleaned_data['veicRenavam']

            item.save()

            return render(request, 'atualizado.html', {})
        
        else:
            return render(request, 'cadastrar_veiculo.html', {'form':form, 'item': item})
    
    elif (request.method == 'GET'):
        return render(request, 'editar_veiculo.html', {'form':form, 'item': item})

def excluir_veiculo(request, nr_item):
    item = get_object_or_404(Veiculo, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

#CLIENTE
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo.html', {})
    
    else:
        form = ClienteForm()
    
    return render(request, 'cadastrar_cliente.html', {'form':form})

def listar_cliente(request):
    lista_itens = Cliente.objects.all()
    return render(request, 'listar_cliente.html', {'lista_itens': lista_itens})

def cliente(request, nr_item):
    cliente = get_object_or_404(Cliente, pk=nr_item)
    return render(request, 'cliente.html', {'item': cliente})

def editar_cliente(request, nr_item):    
    item = get_object_or_404(Cliente, pk=nr_item)
    form = ClienteForm(instance=item)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.clienteCnpj = form.cleaned_data['clienteCnpj']
            item.clienteNome = form.cleaned_data['clienteNome']
            item.clienteRazaoSocial = form.cleaned_data['clienteRazaoSocial']
            item.clienteEnderecoRua = form.cleaned_data['clienteEnderecoRua']
            item.clienteEnderecoNumero = form.cleaned_data['clienteEnderecoNumero']
            item.clienteEnderecoComplemento = form.cleaned_data['clienteEnderecoComplemento']
            item.clienteEnderecoCidade = form.cleaned_data['clienteEnderecoCidade']
            item.clienteEnderecoCep = form.cleaned_data['clienteEnderecoCep']
            item.clienteTelefone = form.cleaned_data['clienteTelefone']
            item.clienteEmail = form.cleaned_data['clienteEmail']
            item.clienteRepresentante = form.cleaned_data['clienteRepresentante']
            item.clienteSegmento = form.cleaned_data['clienteSegmento']
            item.clienteEnderecoEstado = form.cleaned_data['clienteEnderecoEstado']

            item.save()

            return render(request, 'atualizado.html', {})
        
        else:
            return render(request, 'cadastrar_cliente.html', {'form':form, 'item': item})
    
    elif (request.method == 'GET'):
        return render(request, 'editar_cliente.html', {'form':form, 'item': item})

def excluir_cliente(request, nr_item):
    item = get_object_or_404(Cliente, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

#ORDEM DE SERVICO
def cadastrar_os(request):
    if request.method == 'POST':
        form = OSForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo.html', {})
    
    else:
        form = OSForm()
    
    return render(request, 'cadastrar_os.html', {'form':form})

def listar_os(request):
    lista_itens = OrdemDeServico.objects.all()
    return render(request, 'listar_os.html', {'lista_itens': lista_itens})

def ordem_servico(request, nr_item):
    ordem_servico = get_object_or_404(OrdemDeServico, pk=nr_item)
    return render(request, 'ordem_servico.html', {'item': ordem_servico})

def editar_os(request, nr_item):    
    item = get_object_or_404(OrdemDeServico, pk=nr_item)
    form = OSForm(instance=item)
    if request.method == 'POST':
        form = OSForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.osFuncRegistro = form.cleaned_data['osFuncRegistro']
            item.osClienteRegistro = form.cleaned_data['osClienteRegistro']
            item.osVeicRegistro = form.cleaned_data['osVeicRegistro']
            item.osDescricao = form.cleaned_data['osDescricao']
            item.osObservacao = form.cleaned_data['osObservacao']
            item.osOutros = form.cleaned_data['osOutros']
            item.osTipoServico = form.cleaned_data['osTipoServico']

            item.save()

            return render(request, 'atualizado.html', {})
        
        else:
            return render(request, 'cadastrar_os.html', {'form':form, 'item': item})
    
    elif (request.method == 'GET'):
        return render(request, 'editar_os.html', {'form':form, 'item': item})

def excluir_os(request, nr_item):
    item = get_object_or_404(OrdemDeServico, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

def listar_relatorio(request):
    lista_itens = RelatorioDeServico.objects.all()
    return render(request, 'listar_relatorio.html', {'lista_itens': lista_itens})

def relatorio_servico(request, nr_item):
    relatorio_servico = get_object_or_404(RelatorioDeServico, pk=nr_item)
    return render(request, 'relatorio_servico.html', {'item': relatorio_servico})

def excluir_relatorio(request, nr_item):
    item = get_object_or_404(RelatorioDeServico, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')
