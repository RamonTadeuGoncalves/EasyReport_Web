from django import forms
from easyreport_web.models import Funcionario


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
            'funcSobrenome' : 'Sobrenome',
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

