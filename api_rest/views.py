from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from easyreport_web.models import Funcionario, Veiculo, Cliente, OrdemDeServico, RelatorioDeServico, TipoServico
from api_rest.serializers import FuncionarioSerializer, VeiculoSerializer, ClienteSerializer, OSSerializer, \
    RelatorioDeServicoSerializer, UsuarioSerializer, TipoServicoSerializer
from django.contrib.auth.models import User
import base64

# Create your views here.

@csrf_exempt
def loginApi(request, id=0):
    if request.method == 'GET':
        usuario = User.objects.all()
        usuario_serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)

    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)

        if not usuario_serializer.is_valid():
            nomeUsuario = usuario_data['username']
            senhaUsuario = usuario_data['password']
            senha_bytes = senhaUsuario.encode('ascii')
            message_bytes = base64.b64decode(senha_bytes)
            senha_decriptada = message_bytes.decode('ascii')
            # print('Senha decriptada: %s' %(senha_decriptada))
            usuario = authenticate(username=nomeUsuario, password=senha_decriptada)

            if usuario is not None:
                return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED)
            # else:
            #     nomeUsuario = 'userError'
            #     senhaUsuario = 'userError'
            #
            #     user_serializer = UsuarioSerializer(userError, many=True)
            #
            #     userError.delete
            #
            #     return JsonResponse(user_serializer.data, status=status.HTTP_200_OK, safe=False)

        return JsonResponse(usuario_serializer.data, status=status.HTTP_200_OK, safe=False)

@csrf_exempt
def funcionarioApi(request, email='0'):
    if request.method == 'GET':
        funcionario = Funcionario.objects.filter(funcEmail=email)
        funcionario_serializer = FuncionarioSerializer(funcionario, many=True)
        return JsonResponse(funcionario_serializer.data, safe=False)
    elif request.method == 'POST':
        funcionario_data = JSONParser().parse(request)
        funcionario_serializer = FuncionarioSerializer(data=funcionario_data)
        if funcionario_serializer.is_valid():
            funcionario_serializer.save()
            return JsonResponse("Adicionado com Sucesso", safe=False)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        funcionario_data = JSONParser().parse(request)
        funcionario = Funcionario.objects.get(funcRegistro=funcionario_data['funcRegistro'])
        funcionario_serializer = FuncionarioSerializer(funcionario, data=funcionario_data)
        if funcionario_serializer.is_valid():
            funcionario_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        funcionario = Funcionario.objects.get(funcRegistro=id)
        funcionario.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)

@csrf_exempt
def veiculoApi(request, id=0):
    if request.method == 'GET':
        veiculo = Veiculo.objects.all()
        veiculo_serializer = VeiculoSerializer(veiculo, many=True)
        return JsonResponse(veiculo_serializer.data, safe=False)
    elif request.method == 'POST':
        veiculo_data = JSONParser().parse(request)
        veiculo_serializer = VeiculoSerializer(data=veiculo_data)
        if veiculo_serializer.is_valid():
            veiculo_serializer.save()
            return JsonResponse("Adicionado com Sucesso", safe=False)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        veiculo_data = JSONParser().parse(request)
        veiculo = Veiculo.objects.get(funcRegistro=veiculo_data['veicRegistro'])
        veiculo_serializer = VeiculoSerializer(veiculo, data=veiculo_data)
        if veiculo_serializer.is_valid():
            veiculo_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        veiculo = Veiculo.objects.get(veicRegistro=id)
        veiculo.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)

@csrf_exempt
def clienteApi(request, id=0):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(cliente, many=True)
        return JsonResponse(cliente_serializer.data, safe=False)
    elif request.method == 'POST':
        cliente_data = JSONParser().parse(request)
        cliente_serializer = ClienteSerializer(data=cliente_data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Adicionado com Sucesso", safe=False)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        cliente_data = JSONParser().parse(request)
        cliente = Cliente.objects.get(funcRegistro=cliente_data['clienteRegistro'])
        cliente_serializer = ClienteSerializer(cliente, data=cliente_data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        cliente = Cliente.objects.get(clienteRegistro=id)
        cliente.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)

@csrf_exempt
def OSApi(request, id=0):
    if request.method == 'GET':
        ordemDeServico = OrdemDeServico.objects.all()
        ordemDeServico_serializer = OSSerializer(ordemDeServico, many=True)
        return JsonResponse(ordemDeServico_serializer.data, safe=False)
    elif request.method == 'POST':
        ordemDeServico_data = JSONParser().parse(request)
        ordemDeServico_serializer = OSSerializer(data=ordemDeServico_data)
        if ordemDeServico_serializer.is_valid():
            ordemDeServico_serializer.save()
            return JsonResponse("Adicionado com Sucesso", safe=False)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        ordemDeServico_data = JSONParser().parse(request)
        ordemDeServico = OrdemDeServico.objects.get(funcRegistro=ordemDeServico_data['osNumero'])
        ordemDeServico_serializer = OSSerializer(ordemDeServico, data=ordemDeServico_data)
        if ordemDeServico_serializer.is_valid():
            ordemDeServico_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        ordemDeServico = OrdemDeServico.objects.get(osNumero=id)
        ordemDeServico.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)

@csrf_exempt
def RelatorioDeServicoApi(request, id=0):
    if request.method == 'GET':
        relatorioDeServico = RelatorioDeServico.objects.all()
        relatorioDeServico_serializer = RelatorioDeServicoSerializer(relatorioDeServico, many=True)
        return JsonResponse(relatorioDeServico_serializer.data, safe=False)
    elif request.method == 'POST':
        relatorioDeServico_data = JSONParser().parse(request)
        relatorioDeServico_serializer = RelatorioDeServicoSerializer(data=relatorioDeServico_data)
        if relatorioDeServico_serializer.is_valid():
            relatorioDeServico_serializer.save()
            return JsonResponse(relatorioDeServico_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        relatorioDeServico_data = JSONParser().parse(request)
        relatorioDeServico = RelatorioDeServico.objects.get(funcRegistro=relatorioDeServico_data['relatorioNumero'])
        relatorioDeServico_serializer = RelatorioDeServicoSerializer(relatorioDeServico, data=relatorioDeServico_data)
        if relatorioDeServico_serializer.is_valid():
            relatorioDeServico_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        relatorioDeServico = RelatorioDeServico.objects.get(relatorioNumero=id)
        relatorioDeServico.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)

@csrf_exempt
def TipoServicoApi(request, id=0):
    if request.method == 'GET':
        tipoServico = TipoServico.objects.all()
        tipoServico_serializer = TipoServicoSerializer(tipoServico, many=True)
        return JsonResponse(tipoServico_serializer.data, safe=False)
