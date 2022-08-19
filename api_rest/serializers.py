from rest_framework import serializers
from easyreport_web.models import Funcionario, Veiculo, Cliente, OrdemDeServico


class FuncionarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Funcionario
    fields = (
      'funcRegistro', 'funcCpf', 'funcNome',
      'funcEnderecoRua', 'funcEnderecoNumero', 'funcEnderecoComplemento', 'funcEnderecoCidade', 'funcEnderecoCep',
      'funcTelefone', 'funcEmail', 'funcSenha', 'funcFuncao', 'funcDpto', 'funcCnh', 'funcTipoCadastro',
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

