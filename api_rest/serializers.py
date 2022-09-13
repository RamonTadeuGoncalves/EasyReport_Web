from rest_framework import serializers
from easyreport_web.models import Funcionario, Veiculo, Cliente, OrdemDeServico, RelatorioDeServico
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
        'password', 'username',
    )

class FuncionarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Funcionario
    fields = (
      'funcRegistro', 'funcCpf', 'funcNome', 'funcSobrenome',
      'funcEnderecoRua', 'funcEnderecoNumero', 'funcEnderecoComplemento', 'funcEnderecoCidade', 'funcEnderecoCep',
      'funcTelefone', 'funcEmail', 'funcFuncao', 'funcDpto', 'funcCnh', 'funcTipoCadastro',
      'funcEnderecoEstado',
    )

class VeiculoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Veiculo
    fields = (
      'veicRegistro', 'veicPlaca', 'veicModelo', 'veicFabricante', 'veicCor', 'veicRenavam', 'veicAno',
    )


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'clienteRegistro', 'clienteCnpj', 'clienteNome', 'clienteRazaoSocial', 'clienteEnderecoRua', 'clienteEnderecoNumero', 'clienteEnderecoComplemento', 'clienteEnderecoCidade',
            'clienteEnderecoCep', 'clienteTelefone', 'clienteEmail', 'clienteRepresentante', 'clienteSegmento', 'clienteEnderecoEstado'
        )

class OSSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemDeServico
        fields = (
            'osNumero', 'osFuncRegistro', 'osClienteRegistro', 'osVeicRegistro', 'osDataAbertura', 'osDescricao', 'osObservacao', 'osTipoServico', 'osOutros'
        )

class RelatorioDeServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioDeServico

        fields = (
            'relatorioNumero', 'relatorioOsNumero', 'relatorioFuncRegistro', 'relatorioClienteRegistro',
            'relatorioDescricao', 'relatorioContatoCliente', 'relatorioSetorClicente',
            'relatorioData', 'relatorioObservacao', 'relatorioComentarioCliente',
            'relatorioOutros', 'relatorioTipoServico'
        )


