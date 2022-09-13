from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Funcionario(models.Model):
    funcRegistro = models.BigAutoField(primary_key=True)
    funcCpf = models.CharField(max_length=14, unique=True)
    funcNome = models.CharField(max_length=50)
    funcSobrenome = models.CharField(max_length=50)
    funcEnderecoRua = models.CharField(max_length=100)
    funcEnderecoNumero = models.CharField(max_length=10)
    funcEnderecoComplemento = models.CharField(max_length=100, null=True, blank=True)
    funcEnderecoCidade = models.CharField(max_length=50)
    funcEnderecoCep = models.CharField(max_length=10)
    funcTelefone = models.CharField(max_length=20)
    funcEmail = models.CharField(max_length=50)
    # funcSenha = models.CharField(max_length=20)
    # funcConfirmarSenha = models.CharField(max_length=20)
    funcFuncao = models.CharField(max_length=50)
    funcDpto = models.CharField(max_length=50)
    funcCnh = models.BigIntegerField(unique=True)
    tipoCadastro = [
        ('', 'Escolher...'),
        ('Funcionario', 'Funcionario'),
        ('Administrador', 'Administrador')
    ]
    funcTipoCadastro = models.CharField(max_length=15, choices=tipoCadastro, default='')
    estadosBrasileiros = [
    ('', 'Escolher...'),
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ]
    funcEnderecoEstado = models.CharField(max_length=2, choices=estadosBrasileiros, default='')

    class Meta:
        db_table = 'Funcionario'

    def __str__(self):
        return self.funcNome

def current_year():
        return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Veiculo(models.Model):
    veicRegistro = models.BigAutoField(primary_key=True)
    veicPlaca = models.CharField(max_length=8, unique=True)
    veicModelo = models.CharField(max_length=50)
    veicFabricante = models.CharField(max_length=50)
    veicCor = models.CharField(max_length=20)
    veicRenavam = models.BigIntegerField(unique=True)
    veicAno = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])

    class Meta:
        db_table = 'Veiculo'
    
    def __str__(self):
        return str(self.veicPlaca)

class Cliente(models.Model):
    clienteRegistro = models.BigAutoField(primary_key=True)
    clienteCnpj = models.CharField(max_length=20, unique=True)
    clienteNome = models.CharField(max_length=50)
    clienteRazaoSocial = models.CharField(max_length=50)
    clienteEnderecoRua = models.CharField(max_length=100)
    clienteEnderecoNumero = models.CharField(max_length=10)
    clienteEnderecoComplemento = models.CharField(max_length=100, null=True, blank=True)
    clienteEnderecoCidade = models.CharField(max_length=50)
    clienteEnderecoCep = models.CharField(max_length=10)
    clienteTelefone = models.CharField(max_length=20)
    clienteEmail = models.CharField(max_length=50)
    clienteRepresentante = models.CharField(max_length=50)
    clienteSegmento = models.CharField(max_length=50)
    estadosBrasileiros = [
    ('', 'Escolher...'),
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ]
    clienteEnderecoEstado = models.CharField(max_length=2, choices=estadosBrasileiros, default='')
    
    class Meta:
        db_table = 'Cliente'
    
    def __str__(self):
        return self.clienteNome

class OrdemDeServico(models.Model):
    osNumero = models.BigAutoField(primary_key=True)
    osFuncRegistro = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    osClienteRegistro = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    osVeicRegistro = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    osDataAbertura = models.DateField(auto_now=True)
    osDescricao = models.CharField(max_length=200)
    osObservacao = models.CharField(max_length=200, null=True, blank=True)
    osOutros = models.CharField(max_length=100, null=True, blank=True)
    tiposDeServico = [
    ('', 'Escolher...'),
    ('01', 'Manutenção'),
    ('02', 'Manutenção Preventiva'),
    ('03', 'Manutenção Corretiva'),
    ('04', 'Manutenção Preditiva'),
    ('05', 'Vistoria Técnica'),
    ('06', 'Limpeza'),
    ('07', 'Limpeza Ar-condicionado'),
    ('08', 'Treinamento'),
    ('09', 'Outros'),
    ]
    osTipoServico = models.CharField(max_length=100, choices=tiposDeServico, default='')

    class Meta:
        db_table = 'OrdemDeServico'
    
    def __int__(self):
        return self.osNumero
    
    def get_data_ordem_servico(self):
        return self.osDataAbertura.strftime('%d/%m/%Y')

class RelatorioDeServico(models.Model):
    relatorioNumero = models.BigAutoField(primary_key=True)
    relatorioOsNumero = models.ForeignKey(OrdemDeServico, on_delete=models.CASCADE)
    relatorioFuncRegistro = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    relatorioClienteRegistro = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    relatorioDescricao = models.CharField(max_length=200)
    relatorioContatoCliente = models.CharField(max_length=50)
    relatorioSetorClicente = models.CharField(max_length=50)
    relatorioData = models.DateField(auto_now=True)
    # relatorioEstado = models.BooleanField(False)
    relatorioObservacao = models.CharField(max_length=200, null=True, blank=True)
    # relatorioFoto = models.FileField(null=True, blank=True)
    relatorioComentarioCliente = models.CharField(max_length=200, null=True, blank=True)
    relatorioOutros = models.CharField(max_length=100, null=True, blank=True)
    tiposDeServico = [
    ('', 'Escolher...'),
    ('01', 'Manutenção'),
    ('02', 'Manutenção Preventiva'),
    ('03', 'Manutenção Corretiva'),
    ('04', 'Manutenção Preditiva'),
    ('05', 'Vistoria Técnica'),
    ('06', 'Limpeza'),
    ('07', 'Limpeza Ar-condicionado'),
    ('08', 'Treinamento'),
    ('09', 'Outros'),
    ]
    relatorioTipoServico = models.CharField(max_length=100, choices=tiposDeServico, default='')

    class Meta:
        db_table = 'RelatorioDeServico'
    
    def __int__(self):
        return self.relatorioNumero
    
    def get_data_relatorio(self):
        return self.relatorioData.strftime('%d/%m/%Y')
