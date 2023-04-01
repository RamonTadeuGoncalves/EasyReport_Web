from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from validate_docbr import CPF, CNPJ
from authentication.models import Ativacao
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.conf import settings
from easyreport_web.models import *
from easyreport_web.forms import *
from django.contrib.auth.decorators import login_required

mainUrl = ('http://127.0.0.1:8080/')

# Create your views here.
def splash(request):
    return render(request, 'splash.html')

@login_required(login_url='/auth/logar/')
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
                return redirect('index/')
            else:
                usuario
                messages.error(request, 'Você não tem permissão :(')
                logout(request)
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return redirect('/login/')

#USER LOGOUT
@login_required(login_url='/auth/logar/')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/auth/logar/')
def listar_funcionario(request):
    lista_itens = Funcionario.objects.all()
    return render(request, 'listar_funcionario.html', {'lista_itens': lista_itens})

@login_required(login_url='/auth/logar/')
def funcionario(request, nr_item):
    funcionario = get_object_or_404(Funcionario, pk=nr_item)
    return render(request, 'funcionario.html', {'item': funcionario})

@login_required(login_url='/auth/logar/')
def editar_funcionario(request, nr_item):    
    item = get_object_or_404(Funcionario, pk=nr_item)
    
    form = FuncionarioForm(instance=item)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=item)
        cpf = CPF()
        if form.is_valid():
            item = form.save(commit=False)

            item.funcCpf = form.cleaned_data['funcCpf']
            item.funcNome = form.cleaned_data['funcNome']
            item.funcSobrenome = form.cleaned_data['funcSobrenome']
            item.funcEnderecoRua = form.cleaned_data['funcEnderecoRua']
            item.funcEnderecoNumero = form.cleaned_data['funcEnderecoNumero']
            item.funcEnderecoComplemento = form.cleaned_data['funcEnderecoComplemento']
            item.funcEnderecoCidade = form.cleaned_data['funcEnderecoCidade']
            item.funcEnderecoCep = form.cleaned_data['funcEnderecoCep']
            item.funcTelefone = form.cleaned_data['funcTelefone']
            item.funcEmail = form.cleaned_data['funcEmail']
            item.funcFuncao = form.cleaned_data['funcFuncao']
            item.funcDpto = form.cleaned_data['funcDpto']
            item.funcCnh = form.cleaned_data['funcCnh']
            item.funcEnderecoEstado = form.cleaned_data['funcEnderecoEstado']
            item.funcTipoCadastro = form.cleaned_data['funcTipoCadastro']

            user = User.objects.get(id=nr_item)
            user.username = item.funcEmail
            user.email = item.funcEmail

            if not cpf.validate(item.funcCpf):
                messages.add_message(request, constants.ERROR, 'CPF inválido')
                return render(request, 'editar_funcionario.html', {'form':form, 'item': item})
            
            else:            
                user.save()
                item.save()
                return render(request, 'atualizado.html', {})
        
        else:
            return render(request, 'cadastro.html', {'form':form, 'item': item})
    
    elif (request.method == 'GET'):
        return render(request, 'editar_funcionario.html', {'form':form, 'item': item})

@login_required(login_url='/auth/logar/')
def excluir_funcionario(request, nr_item):
    item = get_object_or_404(Funcionario, pk=nr_item)
    autenticacao = Ativacao.objects.get(pk = nr_item)
    autenticacao.delete()
    usuario = User.objects.get(pk = nr_item)
    usuario.delete()
    item.delete()
    return render(request, 'excluido.html')

#VEICULO
@login_required(login_url='/auth/logar/')
def cadastrar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo.html', {})
    
    else:
        form = VeiculoForm()
    
    return render(request, 'cadastrar_veiculo.html', {'form':form})

@login_required(login_url='/auth/logar/')
def listar_veiculo(request):
    lista_itens = Veiculo.objects.all()
    return render(request, 'listar_veiculo.html', {'lista_itens': lista_itens})

@login_required(login_url='/auth/logar/')
def veiculo(request, nr_item):
    veiculo = get_object_or_404(Veiculo, pk=nr_item)
    return render(request, 'veiculo.html', {'item': veiculo})

@login_required(login_url='/auth/logar/')
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

@login_required(login_url='/auth/logar/')
def excluir_veiculo(request, nr_item):
    item = get_object_or_404(Veiculo, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

#CLIENTE
@login_required(login_url='/auth/logar/')
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        cnpj = CNPJ()
        if form.is_valid():
            item = form.save(commit=False)

            item_clienteCnpj = form.cleaned_data['clienteCnpj']

            if not cnpj.validate(item_clienteCnpj):
                messages.add_message(request, constants.ERROR, 'CNPJ inválido')
                return render(request, 'cadastrar_cliente.html', {'form':form})
            else:
                form.save()
                return render(request, 'salvo.html', {})
    
    else:
        form = ClienteForm()
    
    return render(request, 'cadastrar_cliente.html', {'form':form})

@login_required(login_url='/auth/logar/')
def listar_cliente(request):
    lista_itens = Cliente.objects.all()
    return render(request, 'listar_cliente.html', {'lista_itens': lista_itens})

@login_required(login_url='/auth/logar/')
def cliente(request, nr_item):
    cliente = get_object_or_404(Cliente, pk=nr_item)
    return render(request, 'cliente.html', {'item': cliente})

@login_required(login_url='/auth/logar/')
def editar_cliente(request, nr_item):    
    item = get_object_or_404(Cliente, pk=nr_item)
    form = ClienteForm(instance=item)
    cnpj = CNPJ()
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

            if not cnpj.validate(item.clienteCnpj):
                messages.add_message(request, constants.ERROR, 'CNPJ inválido')
                return render(request, 'cadastrar_cliente.html', {'form':form, 'item': item})
            
            else:
                item.save()
                return render(request, 'atualizado.html', {})
        
        else:
            return render(request, 'cadastrar_cliente.html', {'form':form, 'item': item})
    
    elif (request.method == 'GET'):
        return render(request, 'editar_cliente.html', {'form':form, 'item': item})

@login_required(login_url='/auth/logar/')
def excluir_cliente(request, nr_item):
    item = get_object_or_404(Cliente, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

#ORDEM DE SERVICO
@login_required(login_url='/auth/logar/')
def cadastrar_os(request):
    if request.method == 'POST':
        form = OSForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo.html', {})
    
    else:
        form = OSForm()
    
    return render(request, 'cadastrar_os.html', {'form':form})

@login_required(login_url='/auth/logar/')
def listar_os(request):
    lista_itens = OrdemDeServico.objects.all()
    return render(request, 'listar_os.html', {'lista_itens': lista_itens})

@login_required(login_url='/auth/logar/')
def ordem_servico(request, nr_item):
    ordem_servico = get_object_or_404(OrdemDeServico, pk=nr_item)
    return render(request, 'ordem_servico.html', {'item': ordem_servico})

@login_required(login_url='/auth/logar/')
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
            item.osTipoServico = form.cleaned_data['osTipoServico']

            item.save()

            return render(request, 'atualizado.html', {})
        
        else:
            return render(request, 'cadastrar_os.html', {'form':form, 'item': item})
    
    elif (request.method == 'GET'):
        return render(request, 'editar_os.html', {'form':form, 'item': item})

@login_required(login_url='/auth/logar/')
def excluir_os(request, nr_item):
    item = get_object_or_404(OrdemDeServico, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

@login_required(login_url='/auth/logar/')
def listar_relatorio(request):
    lista_itens = RelatorioDeServico.objects.all()
    return render(request, 'listar_relatorio.html', {'lista_itens': lista_itens})

@login_required(login_url='/auth/logar/')
def relatorio_servico(request, nr_item):
    relatorio_servico = get_object_or_404(RelatorioDeServico, pk=nr_item)
    return render(request, 'relatorio_servico.html', {'item': relatorio_servico})

@login_required(login_url='/auth/logar/')
def excluir_relatorio(request, nr_item):
    item = get_object_or_404(RelatorioDeServico, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

@login_required(login_url='/auth/logar/')
def cadastrar_tipo_servico(request):
    if request.method == 'POST':
        form = TipoServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo.html', {})

    else:
        form = TipoServicoForm()

    return render(request, 'cadastrar_tipo_servico.html', {'form': form})

@login_required(login_url='/auth/logar/')
def listar_tipo_servico(request):
    lista_itens = TipoServico.objects.all()
    return render(request, 'listar_tipo_servico.html', {'lista_itens': lista_itens})

@login_required(login_url='/auth/logar/')
def tipo_servico(request, nr_item):
    tipo_servico = get_object_or_404(TipoServico, pk=nr_item)
    return render(request, 'tipo_servico.html', {'item': tipo_servico})

@login_required(login_url='/auth/logar/')
def excluir_tipo_servico(request, nr_item):
    item = get_object_or_404(TipoServico, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')

@login_required(login_url='/auth/logar/')
def editar_tipo_servico(request, nr_item):
    item = get_object_or_404(TipoServico, pk=nr_item)
    form = TipoServicoForm(instance=item)
    if request.method == 'POST':
        form = TipoServicoForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.servDescricao = form.cleaned_data['servDescricao']

            item.save()

            return render(request, 'atualizado.html', {})

        else:
            return render(request, 'cadastrar_tipo_servico.html', {'form': form, 'item': item})

    elif (request.method == 'GET'):
        return render(request, 'editar_tipo_servico.html', {'form': form, 'item': item})
