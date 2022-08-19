from curses import meta
from dataclasses import field, fields
from statistics import mode
from django import forms

from easyreport_web.models import Funcionario, Veiculo, Cliente, OrdemDeServico


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = (
            'funcCpf', 'funcNome',
            'funcEnderecoRua', 'funcEnderecoNumero', 'funcEnderecoComplemento', 'funcEnderecoCidade', 'funcEnderecoCep',
            'funcTelefone', 'funcEmail', 'funcSenha', 'funcFuncao', 'funcDpto', 'funcCnh', 'funcTipoCadastro',
            'funcEnderecoEstado',
        )
        labels = {
            'funcCpf':'CPF',
            'funcNome':'Nome',
            'funcEnderecoRua':'Rua',
            'funcEnderecoNumero':'Número',
            'funcEnderecoComplemento':'Complemento',
            'funcEnderecoCidade':'Cidade',
            'funcEnderecoCep':'CEP',
            'funcTelefone':'Telefone',
            'funcEmail':'E-mail',
            'funcSenha':'Senha',
            'funcFuncao':'Função',
            'funcDpto':'Departamento',
            'funcCnh':'CNH',
            'funcTipoCadastro':'Tipo do Cadastro',
            'funcEnderecoEstado':'Estado',
        }
        widgets = {
            'funcSenha':forms.PasswordInput,
        }

