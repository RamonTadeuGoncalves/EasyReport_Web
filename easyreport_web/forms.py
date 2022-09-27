from django import forms
from .models import Cliente, Funcionario, OrdemDeServico, Veiculo, TipoServico


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = (
            'funcCpf', 'funcNome', 'funcSobrenome',
            'funcEnderecoRua', 'funcEnderecoNumero', 'funcEnderecoComplemento', 'funcEnderecoCidade', 'funcEnderecoCep',
            'funcTelefone', 'funcEmail', 'funcFuncao', 'funcDpto', 'funcCnh', 'funcTipoCadastro',
            'funcEnderecoEstado',
        )
        labels = {
            'funcCpf':'CPF',
            'funcNome':'Nome',
            'funcSobrenome':'Sobrenome',
            'funcEnderecoRua':'Rua',
            'funcEnderecoNumero':'Número',
            'funcEnderecoComplemento':'Complemento',
            'funcEnderecoCidade':'Cidade',
            'funcEnderecoCep':'CEP',
            'funcTelefone':'Telefone',
            'funcEmail':'E-mail',
            'funcFuncao':'Função',
            'funcDpto':'Departamento',
            'funcCnh':'CNH',
            'funcTipoCadastro':'Tipo do Cadastro',
            'funcEnderecoEstado':'Estado',
        }
        # widgets = {
        #     'funcSenha':forms.PasswordInput,
        # }

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = (
            'veicPlaca', 'veicModelo', 'veicFabricante', 'veicCor', 'veicRenavam', 'veicAno'
        )
        labels = {
            'veicPlaca':'Placa',
            'veicModelo':'Modelo',
            'veicFabricante':'Fabricante',
            'veicCor':'Cor',
            'veicRenavam':'Renavam',
            'veicAno':'Ano',
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = (
            'clienteCnpj', 'clienteNome', 'clienteRazaoSocial', 'clienteEnderecoRua', 'clienteEnderecoNumero', 'clienteEnderecoComplemento', 'clienteEnderecoCidade', 'clienteEnderecoCep', 'clienteTelefone', 'clienteEmail', 'clienteRepresentante', 'clienteSegmento', 'clienteEnderecoEstado'
        )
        labels = {
            'clienteCnpj':'CNPJ',
            'clienteNome':'Nome',
            'clienteRazaoSocial':'Razão Social',
            'clienteEnderecoRua': 'Rua',
            'clienteEnderecoNumero':'Número',
            'clienteEnderecoComplemento':'Complemento',
            'clienteEnderecoCidade':'Cidade',
            'clienteEnderecoCep':'CEP',
            'clienteTelefone':'Telefone',
            'clienteEmail':'E-mail',
            'clienteRepresentante':'Responsável/Contato',
            'clienteSegmento':'Segmento',
            'clienteEnderecoEstado':'Estado',
        }

class OSForm(forms.ModelForm):
    class Meta:
        model = OrdemDeServico
        fields = (
            'osFuncRegistro', 'osClienteRegistro', 'osVeicRegistro', 'osDescricao', 'osObservacao', 'osTipoServico', 'osOutros'
        )
        labels = {
            'osFuncRegistro': 'Nome do Funcionário',
            'osClienteRegistro': 'Nome do Cliente',
            'osVeicRegistro': 'Placa do Veiculo',
            'osDescricao':'Descrição',
            'osObservacao':'Observação',
            'osTipoServico':'Tipo de Serviço',
            'osOutros':'Outros',
        }

class TipoServicoForm(forms.ModelForm):
    class Meta:
        model = TipoServico
        fields = (
            'servDescricao',
        )
        labels = {
            'servDescricao':'Tipo de Servico',

        }
